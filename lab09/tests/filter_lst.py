test = {
  'name': 'filter-lst',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter-lst even? '(1 2 3 4))
          eefe2d916ae4b9218d146bc0277a63fa
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(1 3 5))
          7d62d6f97eff3c26faed6c90e572e14b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(2 4 6 1))
          b9d3050f3e734543c211b93d1f4808e8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst even? '(3))
          9fe2321549ca80f78f8bead3784a61a6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? nil)
          9fe2321549ca80f78f8bead3784a61a6
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
