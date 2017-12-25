(define (find s predicate)
  (cond ((null? s) #f)
  	((predicate (car s)) (car s))
  	(else (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (if (null? s) nil
  	(cons-stream (* k (car s)) (scale-stream (cdr-stream s) k))) 
)

(define (has-cycle s)
	(define (check slst stream) 
		(cond ((null? slst) #f)
  			((eq? stream (car slst)) #t)
  			(else (check (cdr-stream slst) stream))))

	(define (checkstream slst stream)
		(cond ((null? stream) #f)
			((check slst stream) #t)
			(else (checkstream (cons-stream stream slst) (cdr-stream stream)))))

		(checkstream nil s))







(define (has-cycle-constant s)
  (define (compare p1 p2)
    (cond ((eq? p1 p2) #t)
          ((or (null? p1) (null? (cdr-stream p1))) #f)
          (else (compare (cdr-stream (cdr-stream p1)) (cdr-stream p2)))))
  (compare (cdr-stream s) s)

)
