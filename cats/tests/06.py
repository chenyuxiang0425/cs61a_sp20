test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> sphinx_swap("car", "cad", big_limit)
          1
          >>> sphinx_swap("this", "that", big_limit)
          2
          >>> sphinx_swap("one", "two", big_limit)
          3
          >>> sphinx_swap("from", "form", big_limit)
          2
          >>> sphinx_swap("awe", "awesome", big_limit)
          4
          >>> sphinx_swap("someawe", "awesome", big_limit)
          6
          >>> sphinx_swap("awful", "awesome", big_limit)
          5
          >>> sphinx_swap("awful", "awesome", 3) > 3
          True
          >>> sphinx_swap("awful", "awesome", 4) > 4
          True
          >>> sphinx_swap("awful", "awesome", 5) > 5
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> sphinx_swap("goodbye", "good", big_limit)
          3
          >>> sphinx_swap("pront", "print", big_limit)
          1
          >>> sphinx_swap("misspollid", "misspelled", big_limit)
          2
          >>> sphinx_swap("worry", "word", big_limit)
          2
          >>> sphinx_swap("first", "flashy", big_limit)
          4
          >>> sphinx_swap("hash", "ash", big_limit)
          4
          >>> sphinx_swap("ash", "hash", big_limit)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "peeling", "gestate", "west",
          ...                     "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, sphinx_swap, 10)
          'peeling'
          >>> autocorrect("abstrction", small_words_list, sphinx_swap, 10)
          'abstract'
          >>> autocorrect("wird", small_words_list, sphinx_swap, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, sphinx_swap, 10)
          'nest'
          >>> # ban iteration
          >>> test.check('cats.py', 'sphinx_swap', ['While', 'For'])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # ***Check that the recursion stops when the limit is reached***
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(sphinx_swap, "someaweqwertyuio", "awesomeasdfghjkl", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('thong', 'thong', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('place', 'wreat', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('pray', 'okee', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('cloit', 'cloit', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('yond', 'yo', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('tb', 'tb', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('gobi', 'gobi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('watap', 'wotapi', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('baffy', 'bafq', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('else', 'konak', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('zygon', 'zrgoi', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('lar', 'lar', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('shop', 'shd', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('pc', 'pc', k) > k for k in range(2)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('sail', 'sail', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('fiber', 'fibe', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('doff', 'do', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('meile', 'meilew', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('donor', 'donorc', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('meet', 'meeu', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('tic', 'tih', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('taft', 'hewer', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('moorn', 'toxa', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('hamal', 'hamal', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('pridy', 'dance', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('dekko', 'ee', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('julio', 'juli', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('boist', 'spume', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('jail', 'jailu', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('cumin', 'goes', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('civil', 'whose', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('stead', 'ny', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('mikie', 'mdkie', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('utils', 'utils', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('nuque', 'nuquv', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('chine', 'ihi', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('tour', 'erase', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('ak', 'rose', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('sawah', 'shape', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('elb', 'logia', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('noily', 'soi', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('fluid', 'grad', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('titer', 'titegw', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('shood', 'shood', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('sher', 'dhey', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('dayal', 'qualm', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('tenai', 'whata', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('bow', 'how', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('tony', 'togqq', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('baby', 'ton', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('seron', 'seron', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('tame', 'tfme', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('kissy', 'kissykd', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('str', 'st', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('enema', 'hnem', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('beden', 'beden', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('coral', 'coral', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('hack', 'haykp', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('alan', 'alan', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('aru', 'aru', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('tail', 'tailp', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('corps', 'co', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('kazi', 'kazi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('bone', 'bone', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('dee', 'dee', k) > k for k in range(3)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('fuder', 'fuder', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('harl', 'harvn', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('def', 'de', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('moio', 'yomo', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('amnia', 'agni', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('pair', 'pair', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('peai', 'seg', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('pryse', 'pryseffp', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('amelu', 'samp', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('weak', 'wea', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('atelo', 'atelo', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('uc', 'kc', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('strew', 'jaup', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('dome', 'dume', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('braze', 'sxaze', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('zaman', 'zaman', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('twank', 'renne', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('pinky', 'pin', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('spoke', 'spoke', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('recto', 'recto', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('ula', 'ula', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('dame', 'froth', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('grane', 'gaane', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('cycad', 'cqcad', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('creem', 'creemibh', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('alky', 'alfy', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('finds', 'fond', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('argot', 'argotlp', k) > k for k in range(7)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('lc', 'roost', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('mi', 'iran', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('faded', 'fadedfeb', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('slee', 'ble', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sphinx_swap('macro', 'macr', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('bbs', 'bbj', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([sphinx_swap('roud', 'roud', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import sphinx_swap, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
