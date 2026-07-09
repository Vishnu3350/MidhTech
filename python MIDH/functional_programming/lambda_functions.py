# Lambda()
#Example 1
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

add = lambda a, b: a + b
print("Addition:", add(num1, num2))

#Example 2
double = lambda x: x * 2
print("Double of the number: ", double(5))

#Example 3
discount_price = lambda price: price - (price * 0.10)
print("Discount of the product price: ", discount_price(1500))

# map()

#Example 1

numbers = [1, 2, 3, 4, 5]

square = list(map(lambda a: a * a, numbers))

print("Square values:", square)

# Example 2

list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]

add = list(map(lambda a, b: a + b, list1, list2))

print("Addition:", add)

#Filter()

marks = [35, 67, 89, 42, 55, 23, 78]

result = list(filter(lambda a: a >= 50, marks))

print("Marks greater than or equal to 50:", result)

# Reduce() 

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a * b, numbers)

print("Multiplication:", result)