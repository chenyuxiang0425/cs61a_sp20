test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from sp20favpets;
          dog|46
          cat|20
          tiger|17
          panda|10
          koala|8
          monkey|8
          penguin|7
          lion|6
          bear|5
          capybara|5
          sqlite> SELECT * from sp20dog;
          dog|46
          sqlite> SELECT * from obedienceimages;
          7|Image 1|22
          7|Image 2|33
          7|Image 3|21
          7|Image 4|44
          7|Image 5|16
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab11
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
