# Average
def average(totalmarks, subjects):
    return totalmarks / subjects

totalmarks = int(input("Enter total marks: "))
subjects = int(input("Enter total subjects: "))

print("The average is: ",average(totalmarks, subjects))


# Arthimetic Operations

def Arthimetic(add=False, sub=False, mul=False, div=False):
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    if add :
        return num1 + num2
    elif sub:
        return num1 - num2
    elif mul:
        return num1 * num2
    elif div:
        return num1 / num2
    else:
        print("Invalid Operation")

print("The addition of two numbers: ", Arthimetic(add = True))
print("The addition of two numbers: ", Arthimetic(sub = True))
print("The addition of two numbers: ", Arthimetic(mul = True))
print("The addition of two numbers: ", Arthimetic(div = True))


# Prime Number

def isprime(n):
    
    if n <=1:
        return False
    for i in range(2, n):
        if n % i == 0 :
            return False
    return True

number = int(input("Enter a number: "))
if isprime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")
