# Example 1
def decorator(func):
    def inner():
        print("Started")

        func()

        print("Ended")

    return inner


@decorator
def display():
    print("Hello Vishnu")


display()

#Example 2

def decorator(func):
    def inner(a, b):
        print("Calculation Started")

        func(a, b)

        print("Calculation Ended")

    return inner


@decorator
def addition(a, b):
    print("Addition:", a + b)


num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

addition(num1, num2)