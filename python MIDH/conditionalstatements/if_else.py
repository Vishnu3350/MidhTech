# Example: Voting Eligibility

age = int(input("Enter your age: ")) 
if (age >= 18):
    print ("Eligible to vote")
else :
    print("Not Eligible")


# Example : check Status 

username = "Vishnu"
logged_in = True

if logged_in :
    print(username, "is Logged into the server")
else :
    print(username, "is not found")

# Example : student passed or failed in an exam 
score = 55
pass_mark = 35

if score == pass_mark or score > pass_mark:
    print("passed")
elif score <= pass_mark:
    print("fail")
else :
    print("Not found")


# Example : Take three values. find that which one of themis min or max

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

maximum = max(a,b,c)
minimum = min(a,b,c)
print("maximum is: ",maximum)
print("minimum is: ",minimum)

# Example : Execute the above program in if-else condition (HOME TASK)

a = 15
b = 5000
c = 1550

if a > b and a > c :
    print("maximum is: ", a)
elif b > c and b > a:
    print("Maximum is: ", b)
else : 
    print("Maximum is: ", c)

    

