"""Web server for the typing GUI."""

import argparse
import json
import socketserver
import ssl
import string
import time
import traceback
import webbrowser

from http import server, HTTPStatus
from http.server import HTTPServer
from random import randrange
from urllib.error import URLError

from ucb import main
from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote, parse_qs

import typing

PORT = 31415
DEFAULT_SERVER = 'https://cats.cs61a.org'
PARAGRAPH_PATH = "./data/sample_paragraphs.txt"
WORDS_LIST = typing.lines_from_file('data/words.txt')
WORDS_SET = set(WORDS_LIST)
LETTER_SETS = [(w, set(w)) for w in WORDS_LIST]
LIMIT = 2
PATHS = {}


def route(path):
    """Register a route handler."""
    def wrap(f):
        PATHS[path] = f
        return f
    return wrap


class Handler(server.BaseHTTPRequestHandler):
    """HTTP handler."""
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        path = "gui/" + unquote(self.path)[1:]
        if "scripts" in path and not path.endswith(".js"):
            path += ".js"

        if path.endswith(".css"):
            self.send_header("Content-type", "text/css")
        elif path.endswith(".js"):
            self.send_header("Content-type", "application/javascript")
        self.end_headers()
        if path == "gui/":
            path = "gui/index.html"
        try:
            with open(path, "rb") as f:  # lol better make sure that port is closed
                self.wfile.write(f.read())
        except Exception as e:
            print(e)
            # raise

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        raw_data = self.rfile.read(content_length)
        data = parse_qs(raw_data.decode("ascii"))
        path = unquote(self.path)

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        try:
            result = PATHS[path](data)
            self.wfile.write(bytes(json.dumps(result), "utf-8"))
        except Exception as e:
            print(e)
            raise

    def log_message(self, *args, **kwargs):
        pass


@route("/request_paragraph")
def request_paragraph(data):
    """Return a random paragraph."""
    paragraphs = typing.lines_from_file(PARAGRAPH_PATH)
    paragraph_index = randrange(len(paragraphs))
    return typing.choose(paragraphs, lambda x: True, paragraph_index)


@route("/analyze")
def compute_accuracy(data):
    """Return [wpm, accuracy]."""
    prompted_text = data["promptedText"][0]
    typed_text = data.get("typedText", [""])[0]
    start_time = float(data["startTime"][0])
    end_time = float(data["endTime"][0])
    return [typing.wpm(typed_text, end_time - start_time),
            typing.accuracy(typed_text, prompted_text)]


def similar(w, v, n):
    """Whether W intersect V contains at least |W|-N and |V|-N elements."""
    intersect = len(w.intersection(v))
    return intersect >= len(w) - n and intersect >= len(v) - n


@route("/autocorrect")
def autocorrect(data):
    """Call autocorrect using the best score function available."""
    raw_word = data.get("word", [""])[0]
    word = typing.lower(typing.remove_punctuation(raw_word))
    if word in WORDS_SET or word == '':
        return raw_word

    # Heuristically choose candidate words to score.
    letters = set(word)
    candidates = [w for w, s in LETTER_SETS if similar(s, letters, LIMIT)]

    # Try various diff functions until one doesn't raise an exception.
    for fn in [typing.final_diff, typing.edit_diff, typing.swap_diff]:
        try:
            guess = typing.autocorrect(word, candidates, fn, LIMIT)
            return reformat(guess, raw_word)
        except BaseException as e:
            pass

    return raw_word


@route("/kill")
def kill(data):
    print("Exiting GUI")
    exit(0)


def reformat(word, raw_word):
    """Reformat WORD to match the capitalization and punctuation of RAW_WORD."""
    # handle capitalization
    if raw_word != "" and raw_word[0].isupper():
        word = word.capitalize()

    # find the boundaries of the raw word
    first = 0
    while first < len(raw_word) and raw_word[first] in string.punctuation:
        first += 1
    last = len(raw_word) - 1
    while last > first and raw_word[last] in string.punctuation:
        last -= 1

    # add wrapping punctuation to the word
    if raw_word != word:
        word = raw_word[:first] + word
        word = word + raw_word[last + 1:]

    return word


###############
# Multiplayer #
###############


def multiplayer_post(path, data, server_url=DEFAULT_SERVER):
    """Post DATA to a multiplayer server PATH and return the response."""
    data_bytes = bytes(urlencode(data, True), encoding='utf-8')
    request = Request(server_url + path, data_bytes, method='POST')
    try:
        response = urlopen(request, context=ssl._create_unverified_context())
        text = response.read().decode('utf-8')
        if text.strip():
            return json.loads(text)
    except Exception as e:
        traceback.print_exc()
        print(e)
        return None


def multiplayer_route(path, server_path=None):
    """Convert a function that takes (data, send) into a route."""
    if not server_path:
        server_path = path
    def wrap(f):
        def send(data):
            return multiplayer_post(server_path, data)
        def routed_fn(data):
            assert typing.enable_multiplayer, 'Multiplayer not implemented; single player only for now'
            response = f(data, send)
            return response
        return route(path)(routed_fn)
    return wrap


def forward_to_server(data, send):
    """Forward a request to the multiplayer server."""
    return send(data)


multiplayer_route("/request_id")(forward_to_server)
multiplayer_route('/request_match')(forward_to_server)
multiplayer_route('/request_progress')(forward_to_server)


@multiplayer_route('/report_progress', '/set_progress')
def report_progress(data, send):
    """Report progress to the multiplayer server and also return it."""
    typed = data.get("typed", [""])[0].split()   # A list of word strings
    prompt = data.get("prompt", [""])[0].split() # A list of word strings
    id = data["id"][0]
    return typing.report_progress(typed, prompt, id, send)


@multiplayer_route('/fastest_words', '/request_all_progress')
def fastest_words(data, send):
    """Return a list of word_speed values describing the game."""
    words = ["START"] + data.get("prompt", [""])[0].split()
    del data["prompt"]
    progress = send(data)
    start_times = [p[0][1] for p in progress]
    word_times = [[typing.word_time(w, p[1] - s) for w, p in zip(words, ps)] \
                  for s, ps in zip(start_times, progress)]

    return typing.fastest_words_report(word_times)


@main
def start(*args):
    """Start web server."""
    parser = argparse.ArgumentParser(description="Cats GUI Server")
    parser.add_argument('-s', help="Stand-alone: do not open browser", action='store_true')
    args = parser.parse_args()

    request = Request("http://127.0.0.1:{}/kill".format(PORT), method='POST')
    try:
        urlopen(request)
        print("Killing existing gui process...")
        time.sleep(1)
    except URLError:
        pass

    socketserver.TCPServer.allow_reuse_address = True
    httpd = HTTPServer(("127.0.0.1", PORT), Handler)
    if not args.s:
        webbrowser.open("http://127.0.0.1:" + str(PORT), new=0, autoraise=True)
    httpd.serve_forever()