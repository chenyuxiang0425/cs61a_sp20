test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((= 1 1) 42))
          34dfc44372e994d7835c6ef2cfac97d7
          # locked
          scm> (cond ((= 1 1) 42) ((= 1 1) 24))
          34dfc44372e994d7835c6ef2cfac97d7
          # locked
          scm> (cond ((= 1 0) 42) ((= 0 1) 24) (else 999))
          3a6f3955d5dc68b6b7a04fd9398246ac
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign -42)
          f89b9122342dc0cbae1551c4e7433fb3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 0)
          64f0ad851d7646afffbc5722e153b4ed
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 42)
          a904eba72e14d658e2e8f72792dd3944
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
