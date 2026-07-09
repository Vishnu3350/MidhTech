#Example 1

def numbers(num):
    for i in range(1, num + 1):
        yield i

num = int(input("Enter the number: "))

values = numbers(num)

for i in values:
    print(i)

# EXample 2

def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter the number: "))

result = even_numbers(n)

for i in result:
    print(i)