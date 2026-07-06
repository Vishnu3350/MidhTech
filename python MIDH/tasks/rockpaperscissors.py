import random   #Imports the random module. We use it to make the system choose randomly.

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ")
system = random.choice(choices)

print("Your choice:", user)
print("System choice:", system)

if user == system:
    print("Match Tie")

elif user == "rock" and system == "scissors":
    print("You Win")

elif user == "paper" and system == "rock":
    print("You Win")

elif user == "scissors" and system == "paper":
    print("You Win")

elif user not in choices:
    print("Invalid Choice")

else:
    print("System Win")