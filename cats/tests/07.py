test = {
  'name': 'Problem 7',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> edit_diff("wird", "wiry", big_limit)
          1
          >>> edit_diff("wird", "bird", big_limit)
          1
          >>> edit_diff("wird", "wir", big_limit)
          1
          >>> edit_diff("wird", "bwird", big_limit)
          1
          >>> edit_diff("speling", "spelling", big_limit)
          1
          >>> edit_diff("used", "use", big_limit)
          1
          >>> edit_diff("hash", "ash", big_limit)
          1
          >>> edit_diff("ash", "hash", big_limit)
          1
          >>> edit_diff("roses", "arose", big_limit)     # roses -> aroses -> arose
          2
          >>> edit_diff("tesng", "testing", big_limit)   # tesng -> testng -> testing
          2
          >>> edit_diff("rlogcul", "logical", big_limit) # rlogcul -> logcul -> logicul -> logical
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "wire", "peeling", "gestate",
          ...                     "west", "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, edit_diff, 10)
          'spelling'
          >>> autocorrect("abstrction", small_words_list, edit_diff, 10)
          'abstraction'
          >>> autocorrect("wird", small_words_list, edit_diff, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, edit_diff, 10)
          'nest'
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
          ...     trace.Trace(trace=True).runfunc(edit_diff, "someawe", "awesome", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 1000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('thong', 'thong', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('place', 'wreat', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('pray', 'okee', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('cloit', 'cloit', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('yond', 'snd', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('tb', 'tb', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('gobi', 'gobi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('watap', 'woitap', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('baffy', 'btfi', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('else', 'konak', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('zygon', 'jzon', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('lar', 'lar', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('shop', 'wopd', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('pc', 'pc', k) > k for k in range(2)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('sail', 'sail', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('fiber', 'fbk', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('doff', 'def', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('meile', 'mqeile', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('donor', 'doinor', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('meet', 'meeu', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('tic', 'tih', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('taft', 'hewer', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('moorn', 'toxa', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('hamal', 'hamal', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('pridy', 'dance', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('dekko', 'zbk', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('julio', 'juio', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('boist', 'spume', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('jail', 'jaila', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('cumin', 'goes', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('civil', 'whose', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('stead', 'ny', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('mikie', 'mdiye', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('utils', 'utils', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('nuque', 'nuq', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('chine', 'ziinx', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('tour', 'erase', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('ak', 'rose', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('sawah', 'shape', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('elb', 'logia', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('noily', 'oibs', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('fluid', 'grad', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('titer', 'tskhteur', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('shood', 'shood', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('sher', 'xdhe', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('dayal', 'qualm', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('tenai', 'whata', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('bow', 'how', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('tony', 'togqq', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('baby', 'ton', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('seron', 'seron', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('tame', 'tfme', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('kissy', 'kisdsxk', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('str', 'st', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('enema', 'nemr', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('beden', 'beden', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('coral', 'coral', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('hack', 'rhack', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('alan', 'alan', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('aru', 'aru', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('tail', 'taiil', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('corps', 'ckcp', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('kazi', 'kazi', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('bone', 'bone', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('dee', 'derv', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('fuder', 'fuder', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('harl', 'hhtar', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('def', 'df', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('moio', 'yomo', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('amnia', 'wna', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('pair', 'pair', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('peai', 'eabi', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('pryse', 'prysvf', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('amelu', 'samp', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('weak', 'wk', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('atelo', 'atelo', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('uc', 'kc', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('strew', 'jaup', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('dome', 'dume', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('braze', 'sxaze', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('zaman', 'zadpamn', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('twank', 'renne', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('pinky', 'opiky', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('spoke', 'spoke', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('recto', 'recto', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('ula', 'ula', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('dame', 'froth', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('grane', 'griae', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('cycad', 'cqcad', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('creem', 'ashreem', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('alky', 'alfy', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('finds', 'fid', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('argot', 'arxgot', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('lc', 'roost', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('mi', 'iran', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('faded', 'fabehc', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('slee', 'ble', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> edit_diff('macro', 'macr', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('bbs', 'bbj', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([edit_diff('roud', 'roud', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import edit_diff, autocorrect
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
