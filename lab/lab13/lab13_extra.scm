;; More Scheme ;;

(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

(define (tally names)
  (cond ((null?names) nil)
      ((null? (cdr names)) (cons (car names)))
)


; Using this helper procedure is optional. You are allowed to delete it. 


(define (unique s)
  (cond ((null? s) nil)
      ((null? (cdr s)) s)
      ((equal? (car s) (car (cdr s))) )
      )
)
; Using this helper procedure is optional. You are allowed to delete it.
(define (count name s)
  (cond ((null? s) nil)
        ((equal? (car s) name) (+ 1 (count name (cdr s))))
        (else (count name (cdr s))))
)

;; Streams ;;

(define (rle s)
  'YOUR-CODE-HERE
)

;; For Testing Purposes

(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)
(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)