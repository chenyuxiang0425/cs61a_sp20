test = {
  'name': 'remove',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (remove 3 nil)
          9fe2321549ca80f78f8bead3784a61a6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 2 '(1 3 2))
          81408d5fa279ca90f14990b7fb691739
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 1 '(1 3 2))
          3ef661a6e5fe509388b944d93a6986d1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 42 '(1 3 2))
          9d4431bea9ae2388a64e18e8a3904a3d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 3 '(1 3 3 7))
          0a27efd98d33a7265c206063eaca5597
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
