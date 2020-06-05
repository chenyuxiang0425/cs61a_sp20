test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> swap_diff("car", "cad", big_limit)
          52f1b72ba99dddc798bb5cebce0be695
          # locked
          >>> swap_diff("this", "that", big_limit)
          45c27a29bbaeb163dec9a0eaed9c7c9c
          # locked
          >>> swap_diff("one", "two", big_limit)
          91711de69bc1d16e478231c51fac5db8
          # locked
          >>> swap_diff("from", "form", big_limit)
          45c27a29bbaeb163dec9a0eaed9c7c9c
          # locked
          >>> swap_diff("awe", "awesome", big_limit)
          bfdc03a3c261c5dc71255ec79dd5977e
          # locked
          >>> swap_diff("someawe", "awesome", big_limit)
          ca82d3ac444a7724c7a6f8a337e495f5
          # locked
          >>> swap_diff("awful", "awesome", big_limit)
          f29bb7189bc0116caaaf05635899b49b
          # locked
          >>> swap_diff("awful", "awesome", 3) > 3
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> swap_diff("awful", "awesome", 4) > 4
          f0a7036a7438d73054555da0482ad042
          # locked
          >>> swap_diff("awful", "awesome", 5) > 5
          81e16d9126cb46b28abbb0a979cb030a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> swap_diff("goodbye", "good", big_limit)
          3
          >>> swap_diff("pront", "print", big_limit)
          1
          >>> swap_diff("misspollid", "misspelled", big_limit)
          2
          >>> swap_diff("worry", "word", big_limit)
          2
          >>> swap_diff("first", "flashy", big_limit)
          4
          >>> swap_diff("hash", "ash", big_limit)
          4
          >>> swap_diff("ash", "hash", big_limit)
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
          >>> autocorrect("speling", small_words_list, swap_diff, 10)
          'peeling'
          >>> autocorrect("abstrction", small_words_list, swap_diff, 10)
          'abstract'
          >>> autocorrect("wird", small_words_list, swap_diff, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, swap_diff, 10)
          'nest'
          >>> # ban iteration
          >>> test.check('typing.py', 'swap_diff', ['While', 'For'])
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
          ...     trace.Trace(trace=True).runfunc(swap_diff, "someaweqwertyuio", "awesomeasdfghjkl", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('thong', 'thong', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('place', 'wreat', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('pray', 'okee', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('cloit', 'cloit', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('yond', 'yo', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('tb', 'tb', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('gobi', 'gobi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('watap', 'wotapi', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('baffy', 'bafq', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('else', 'konak', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('zygon', 'zrgoi', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('lar', 'lar', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('shop', 'shd', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('pc', 'pc', k) > k for k in range(2)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('sail', 'sail', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('fiber', 'fibe', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('doff', 'do', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('meile', 'meilew', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('donor', 'donorc', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('meet', 'meeu', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('tic', 'tih', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('taft', 'hewer', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('moorn', 'toxa', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('hamal', 'hamal', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('pridy', 'dance', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('dekko', 'ee', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('julio', 'juli', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('boist', 'spume', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('jail', 'jailu', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('cumin', 'goes', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('civil', 'whose', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('stead', 'ny', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('mikie', 'mdkie', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('utils', 'utils', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('nuque', 'nuquv', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('chine', 'ihi', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('tour', 'erase', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('ak', 'rose', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('sawah', 'shape', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('elb', 'logia', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('noily', 'soi', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('fluid', 'grad', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('titer', 'titegw', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('shood', 'shood', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('sher', 'dhey', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('dayal', 'qualm', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('tenai', 'whata', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('bow', 'how', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('tony', 'togqq', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('baby', 'ton', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('seron', 'seron', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('tame', 'tfme', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('kissy', 'kissykd', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('str', 'st', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('enema', 'hnem', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('beden', 'beden', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('coral', 'coral', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('hack', 'haykp', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('alan', 'alan', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('aru', 'aru', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('tail', 'tailp', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('corps', 'co', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('kazi', 'kazi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('bone', 'bone', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('dee', 'dee', k) > k for k in range(3)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('fuder', 'fuder', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('harl', 'harvn', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('def', 'de', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('moio', 'yomo', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('amnia', 'agni', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('pair', 'pair', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('peai', 'seg', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('pryse', 'pryseffp', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('amelu', 'samp', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('weak', 'wea', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('atelo', 'atelo', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('uc', 'kc', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('strew', 'jaup', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('dome', 'dume', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('braze', 'sxaze', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('zaman', 'zaman', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('twank', 'renne', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('pinky', 'pin', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('spoke', 'spoke', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('recto', 'recto', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('ula', 'ula', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('dame', 'froth', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('grane', 'gaane', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('cycad', 'cqcad', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('creem', 'creemibh', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('alky', 'alfy', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('finds', 'fond', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('argot', 'argotlp', k) > k for k in range(7)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('lc', 'roost', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('mi', 'iran', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('faded', 'fadedfeb', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('slee', 'ble', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('macro', 'macr', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('bbs', 'bbj', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('roud', 'roud', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import swap_diff, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
