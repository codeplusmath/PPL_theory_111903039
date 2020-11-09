x = int(input("Enter number to be divided: "))
try:
    y = int(input("Enter number to divide with: "))
    quotient = x / y

except ZeroDivisionError:
    print("ZeroDivisonError: Division with 0 is not permitted")

else:
    print("Result = ", quotient)
