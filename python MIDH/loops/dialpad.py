dialpad = "* 0 #"
row = int(input("Enter the rows: "))
column = int(input("Enter the columns: "))
count = 1
for i in range(row):
    for j in range(column):
        print(count , end= " ")
        count+=1
    print()
print(dialpad)

   