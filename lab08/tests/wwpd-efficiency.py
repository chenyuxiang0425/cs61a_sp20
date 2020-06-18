test = {
  'name': 'Orders of Growth',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '6f968a7981449f66717a39a4fb8e2b85',
          'choices': [
            'Logarithmic',
            'Linear',
            'Quadratic',
            'Exponential'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the order of growth of `is_prime` in terms of `n`?
          
          def is_prime(n):
              for i in range(2, n):
                  if n % i == 0:
                      return False
              return True
          """
        },
        {
          'answer': '2c6cd1fa356c89d41c835e6864176471',
          'choices': [
            'Logarithmic',
            'Linear',
            'Quadratic',
            'Exponential'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the order of growth of `bar` in terms of `n`?
          
          def bar(n):
              i, sum = 1, 0
              while i <= n:
                  sum += biz(n)
                  i += 1
              return sum
          
          def biz(n):
              i, sum = 1, 0
              while i <= n:
                  sum += i**3
                  i += 1
              return sum
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
