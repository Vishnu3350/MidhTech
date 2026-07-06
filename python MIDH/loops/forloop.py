
for number in range(1 , 7):
    print(number)

students = ["vishnu", "rakesh", "karthik", "nani"]
print("After the loop executes: ", students)


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for i in range (rows):
    for j in range(cols):
        print(symbol, end=" ")
    print()

