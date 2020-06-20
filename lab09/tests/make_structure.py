test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a '(1))
          bd3f05fa4cb9864ae23adf7936df4482
          # locked
          scm> a
          b9d3050f3e734543c211b93d1f4808e8
          # locked
          scm> (define b (cons 2 a))
          90e805b4bb15ef8854fd5ccbb0d9601f
          # locked
          scm> b
          1950181d4be407b7d109809a1722eb97
          # locked
          scm> (define c (list 3 b))
          c7b5a5707e50e9a75b69a2b365646bab
          # locked
          scm> c
          e6692c1ebab7ee77215df9cc0ad3e1e5
          # locked
          scm> (car c)
          7cce957d5689f75737e35919f54283e1
          # locked
          scm> (cdr c)
          3b4e95240ede6a3fa460a5c068893f37
          # locked
          scm> (car (car (cdr c)))
          32cd207d18df99546ca7a56bc36ed715
          # locked
          scm> (cdr (car (cdr c)))
          b9d3050f3e734543c211b93d1f4808e8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> lst  ; type out exactly how Scheme would print the list
          1a640fc457289f479fdf762e3f43325d
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
