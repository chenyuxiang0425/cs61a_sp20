test = {
  'name': 'Prologue - Reader',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '8006978b69e088213a68a29f96d158db',
          'choices': [
            'Read-Eval-Print-Loop',
            'Really-Enormous-Purple-Llamas',
            'Read-Eval-Parse-Lex'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does REPL stand for?'
        },
        {
          'answer': '560dfb9ee5e254242e7befdf431a9a4b',
          'choices': [
            'Evaluates call expressions',
            'Turns input into tokens',
            'Ensures a function has been defined before it is called',
            'Turns input into a useful data structure'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the read component of the REPL loop do?'
        },
        {
          'answer': 'f83a3686282b92ecbd9b45a40e8f7184',
          'choices': [
            'Input expression with corrected number of parentheses',
            'Input expression represented as a list of tokens',
            'Input expression represented as an instance of a subclass of Expr',
            'Result of evaluating the input expression'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the tokenize function in reader.py return?'
        },
        {
          'answer': '7b3642c4375ddd3e2937ee44e3f9e199',
          'choices': [
            "['add', '(', 3, ',', 4, ')']",
            "['a', 'd', 'd', '(', '3', ',', '4', ')']",
            "['add', '(', '3', ',', '4', ')']",
            "['a', 'd', 'd', '(', 3, ',', 4, ')']"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will tokenize('add(3, 4)') output?"
        },
        {
          'answer': '09ca4840525f7705cc497bab8a1540d9',
          'choices': [
            "['(', LambdaExpr, 4, ')', '(', ')']",
            "['lambda', 4, '(', ')']",
            "['(', 'lambda', ':', 4, ')', '(', ')']",
            "['(', LambdaExpr, ':', 4, ')', '(', ')']"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will tokenize('(lambda: 4)()') output?"
        },
        {
          'answer': '87023482ce5763d6af59c0e0b46081ff',
          'choices': [
            'List of tokens and number of parentheses',
            'Input expression and list of tokens',
            'List of tokens and an instance of a subclass of Expr',
            'Input expression and an instance of a subclass of Expr'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What does the read_expr function in reader.py accept as input and
          return?  (looking at the read function may help answer this question)
          """
        },
        {
          'answer': '56aae11ea5ef1e4430150e37b6afcc60',
          'choices': [
            'Input expression with corrected number of parentheses',
            'Input expression represented as a list of tokens',
            'Input expression represented as an instance of a subclass of Expr',
            'Result of evaluating the input expression'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the read function in reader.py return?'
        },
        {
          'answer': 'c8719397b67eeba8c4826370e9fcc052',
          'choices': [
            'Literal(1)',
            'Number(1)',
            "Name('1')",
            'Name(1)'
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('1') output?"
        },
        {
          'answer': 'fd0cb816ca4bc1c16a1b18d7c9899909',
          'choices': [
            'Literal(x)',
            'x',
            'Name(x)',
            "Name('x')"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('x') output?"
        },
        {
          'answer': '9964a5ee1d418d42c046ba51a5d20093',
          'choices': [
            "CallExpr(Literal('add'), Literal(3), Literal(4))",
            "CallExpr('add', [Literal(3), Literal(4)])",
            "CallExpr(Name('add'), Literal(3), Literal(4))",
            "CallExpr(Name('add'), [Literal(3), Literal(4)])"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('add(3, 4)') output?"
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
