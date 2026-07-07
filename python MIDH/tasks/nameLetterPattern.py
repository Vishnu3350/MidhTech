row = int(input("Enter the number of rows: "))

for i in range(row):
    for j in range(row * 2):
        if j == i or j == row * 2 - i - 2:
            print("v", end="")
        else:
            print(" ", end="")
    print()