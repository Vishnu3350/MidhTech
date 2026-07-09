file = open("student.txt", "a")

name = input("Enter student name: ")
marks = input("Enter marks: ")

file.write("Name: " + name + ", Marks: " + marks + "\n")

file.close()

print("Student record added successfully")

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()