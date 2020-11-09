
(defun factorial (num)
(if (<= num 1) 1 (* num (factorial (- num 1)))))
(princ "Program to return factorial of number")
; this inserts a new line ,it stands for terminating print
(terpri)
(princ "Enter number whose factorial is to be calculated: ")
(setq n (read))
(princ "Factorial is: ")
(write (factorial n))