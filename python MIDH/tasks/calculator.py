operation = input("Select the operator +, -, *, /, %, ^: ")
num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1/num2
elif operation == "%":
    result = num1%num2
else:
    result = num1 ^ num2


print(result)