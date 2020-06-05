test = {
  'name': 'List Indexing',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 3, [5, 7], 9] # Write the expression that indexes into x to output the 7
          a3125442f2585c4dc7f3ced46c1fcaab
          # locked
          >>> x = [[3, [5, 7], 9]] # Write the expression that indexes into x to output the 7
          caafb1bc451eaace7408a7513a8b7502
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lst = [3, 2, 7, [84, 83, 82]]
          >>> lst[4]
          66901ed5775b51743d745870a1a883e3
          # locked
          >>> lst[3][0]
          fb50293c27bf0293f83a92927172e455
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
