class Student():
    def __init__(self,name,age, number, address, rollno):
        self.name = name
        self.age = age
        self.number = number
        self.address = address
        self.rollno = rollno
    def display(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)
        print("Address is: ",self.address)
        print("Number is: ",self.number)
        print("ROllNO is: ",self.rollno)

s1 = Student("Vishnu", 23, "Nellore", 9866280734, 50)
s1.display()