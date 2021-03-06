;; Extra Scheme Questions ;;


; Q5
(define lst
  (list (cons 1 nil) 2 (cons 3 4) 5)
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (filter (lambda (x) (not (= x item))) lst )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
	(define mi (min a b))
	(define ma (max a b))
	(cond 
		((= mi 0) ma)
		((= (modulo ma mi) 0) mi)
		(else (gcd mi (modulo ma mi))))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
	(define helper (lambda (x) (not (= x (car s)))))
	(cond
		((null? s) s)
		; ((null? (filter helper (cdr s))) (list (car s)))
  		(else (cons (car s) (no-repeats (filter helper (cdr s))))))

)

; Q10
(define (substitute s old new)
  (cond
  	((null? s) s)
  	((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
  	((equal? (car s) old) (cons new (substitute (cdr s) old new)))
  	(else (cons (car s) (substitute (cdr s) old new))))
)

; Q11
(define (sub-all s olds news)
	(if (null? olds)
		s
		(sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))) 
)
