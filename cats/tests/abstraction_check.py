"""Infrastructure for detecting abstraction barrier violations."""

class AbstractionViolation(Exception):
    pass

def datatype(obj):
    return type(obj).__name__

# Generic abstract data type
class Abstract(object):
    def __add__(self, other):
        raise AbstractionViolation("Can't add {} object to {}".format(datatype(self), datatype(other)))

    def __radd__(self, other):
        raise AbstractionViolation("Can't add {} object to {}".format(datatype(self), datatype(other)))

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return other is self
        raise AbstractionViolation("Can't use == on {} object and {}".format(datatype(self), datatype(other)))

    def __ne__(self, other):
        if isinstance(other, type(self)):
            return other is not self
        raise AbstractionViolation("Can't use != on {} object and {}".format(datatype(self), datatype(other)))

    def __bool__(self):
        raise AbstractionViolation("Can't use {} object as a boolean".format(datatype(self)))

    def __getitem__(self, index):
        raise AbstractionViolation("Can't use [] notation on {} object".format(datatype(self)))

    def __contains__(self, other):
        raise AbstractionViolation("Can't use contains notation on {} object".format(datatype(self)))

    def __delitem__(self, other):
        raise AbstractionViolation("Can't use del notation on {} object".format(datatype(self)))

    def __iter__(self):
        raise AbstractionViolation("Can't iterate on {} object".format(datatype(self)))

    def __len__(self):
        raise AbstractionViolation("Can't use len notation on {} object".format(datatype(self)))

    def __setitem__(self, key, item):
        raise AbstractionViolation("Can't use setitem notation on {} object".format(datatype(self)))

    def __call__(self, *args, **kwargs):
        raise AbstractionViolation("Can't call {} object".format(datatype(self)))

    def __hash__(self):
        return id(self)

class WordTime(Abstract):
    def __init__(self, word, time):
        self.a, self.b = word, time
    def __repr__(self):
        return '<WordTime {} {}>'.format(self.a, self.b)

word_time = WordTime
word = lambda u: u.a
elapsed_time = lambda u: u.b

old = {}

def swap_implementations(impl):
    # save other implementations
    old['word_time'] = impl.word_time, impl.word, impl.elapsed_time

    # save our implementations
    new_word_time = word_time, word, elapsed_time

    # replace impl's implementations with ours
    impl.word_time, impl.word, impl.elapsed_time = word_time, word, elapsed_time

def restore_implementations(impl):
    impl.word_time, impl.word, impl.elapsed_time = old['word_time']
