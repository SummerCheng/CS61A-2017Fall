;; Scheme ;;
(define (compose-all funcs)
  (cond
  	((null? funcs) (lambda (x) x)) 
  	((null? (cdr funcs)) (car funcs))

  	(else (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)))))
)

(define (deep-map fn s)
   (cond ((null? s) nil)
   		((list? s) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
   		(else (fn s))
   		)
)
