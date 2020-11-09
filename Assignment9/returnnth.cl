(princ "Program to return nth element of the list")
; this inserts a new line ,it stands for terminating print
(terpri)
(princ "Enter the list with parenthesis:")
(setq l (read))
(princ "Enter the value of n: ")
(setq n (read))
(princ "The element is: ")
(write (car (nthcdr (- n 1) l)))
