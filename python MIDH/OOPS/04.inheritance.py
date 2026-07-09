class animal:
    def eat(self):
        print("Animal eats food")

class dog(animal):
    def bark(self):
        print("Dog Barks")

class cat(animal):
    def sound(self):
        print("cat sounds meow")

class lion(animal):
    def roar(self):
        print("Lion roar")


dog1 = dog()
dog1.eat()
dog1.bark()

lion1 = lion()
lion1.eat()
lion1.roar()

cat1 = cat()
cat1.eat()
cat1.sound()

