operator = input("Choose an operator among (+ - * /) : ")

num1 = float(input(("Enter first number : ")))
num2 = float(input(("Enter second number : ")))

if operator == '+':
    result = num1 + num2
    print(round(result,2))
elif operator == '-':
    result = num1 - num2
    print(round(result,2))
elif operator == '*':
    result = num1 * num2
    print(round(result,2))
elif operator == '/':
    result = num1 / num2
    print(round(result,2))
else :
    print(f"{operator} is not a valid operator")
    