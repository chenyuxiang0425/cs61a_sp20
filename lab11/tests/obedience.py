test = {
  'name': 'obedience',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          7|Image 4
          the number 7 below.|Image 1
          seven|Image 3
          the number 7 below.|Image 1
          the number 7 below.|Image 4
          the number 7 below.|Image 4
          the number 7 below.|Image 2
          7|Image 3
          the number 7 below.|Image 5
          7|Image 3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab11.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
