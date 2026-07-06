count = 10

while count >= 0:
    print(count)
    count -= 1


#Task

Food_items = ["pizza", "biryani", "burger", "chicken"]

while True :
    food = input("Enter your food item(press q to quit): ")
    if food == "q":
        print ("Thankyou")
        break
    elif food in Food_items:
        print("you like", food)
    else:
        print("food item not found")
    
rating = int(input("Enter the review b/w 1-10: "))
if(rating <=10):
    print("You have given: ",rating)
else:
    print("Invalid Number")


    