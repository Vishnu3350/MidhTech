import random

system = random.randint(1, 100) #a function in Python that generates a random integer number within a given range.
count = 0

while True:
    user = int(input("Enter your guess between 1 to 100: "))
    count = count + 1
 
    if user == system:
        print("Correct Guess")
        print("You guessed in", count, "attempts")
        break

    elif user < system:
        print("Your guess is low")

    else:
        print("Your guess is high")