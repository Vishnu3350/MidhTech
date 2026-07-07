import math

operation = input("Select operation +, -, *, /, %, **, //, square, cube, sqrt, cbrt, root, inverse, factorial, sin, cos, tan, 10power, pi: ")

num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))


if operation == "+": 
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
elif operation == "%":
    result = num1 % num2
elif operation == "**":
    result = num1 ** num2
elif operation == "//":
    result = num1 // num2
elif operation == "square":
    result = num1 ** 2, num2 ** 2
elif operation == "cube":
    result = num1 ** 3, num2 ** 3
elif operation == "sqrt":
    result = math.sqrt(num1), math.sqrt(num2)
elif operation == "cbrt":
    result = math.cbrt(num1), math.cbrt(num2)
elif operation == "root":
    result = num1 ** (1 / num2)
elif operation == "inverse":
    result = 1 / num1 , 1 / num2
elif operation == "factorial":
    result = math.factorial(int(num1)), math.factorial(int(num2))
elif operation == "sin":
    result = math.sin(math.radians(num1)), math.sin(math.radians(num2))
elif operation == "cos":
    result = math.cos(math.radians(num1)), math.cos(math.radians(num2))
elif operation == "tan":
    result = math.tan(math.radians(num1)), math.tan(math.radians(num2)) 
elif operation == "10power":
    result = 10 ** num1, 10 ** num2 
elif operation == "pi":
    result = math.pi
else:
    result = "Invalid operator"


print(result)