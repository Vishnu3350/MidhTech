class Student:
    def __init__(self):
        self.name = "Vishnu"      
        self._age = 23             
        self.__marks = 85         

    def display(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Marks:", self.__marks)


s1 = Student()

print(s1.name)       
print(s1._age)       

s1.display()         