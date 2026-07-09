try:
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Number cannot be divided by zero")

except ValueError:
    print("Please enter numbers only")