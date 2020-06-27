; Lab 14: Final Review

(define (compose-all funcs)
  (lambda (x)
  (if (null? funcs)
    x
    ((compose-all (cdr funcs))((car funcs) x)))))