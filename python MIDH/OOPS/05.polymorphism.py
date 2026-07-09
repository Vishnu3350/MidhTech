class Animal:
    def sound(self):
        print("Animals can sound")
class Dog:
    def sound(self):
        print("Dog Barks")

class Cat:
    def sound(self):
        print("Cat Meows")

animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()


# Example 2

def add(a, b=1, c=2):
    return a + b + c

print("add(5)", add(5))
print("add(5, 10)", add(5, 10))
print("add(5, 10, 15)", add(5, 10, 15))