operation = input("Select the operator +, -, *, /, %, ^, ci: ")

num1 = float(input("Enter number1 / Principal amount: "))
num2 = float(input("Enter number2 / Rate of interest: "))

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    result = num1 / num2

elif operation == "%":
    result = (num1 * num2) / 100

elif operation == "^":
    result = num1 ** num2

elif operation == "ci":
    time = float(input("Enter time in years: "))
    amount = num1 * (1 + num2 / 100) ** time
    result = amount - num1

else:
    result = "Invalid operation"

print("Result:", result)