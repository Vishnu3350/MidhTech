# Student record using encapsulation
print("Using Encapsulation")
class S_record:
    def __init__(self, name, age, marks, result):
        self.name = name
        self.__age = age
        self._marks = marks
        self.result = result
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.__age)
        print("Marks: ",self._marks)
        print("Result: ",self.result)

Student = S_record("Vishnu", 23, 85, "Pass")
Student.display()

print("Using Inhertence")
# Student record using Inheritence
class student:
    def record(self):
        print("Student Details")
class name(student):
    def s_name(self):
        print("Name: Vishnu")
class age(student):
    def s_age(self):
        print("Age: 23")
class marks(student):
    def s_marks(self):
        print("Marks: 85")
class result(student):
    def s_result(self):
        print("Result: Pass")

name1 = name()
name1.s_name()

age1 = age()
age1.s_age()

mark = marks()
mark.s_marks()

result1 = result()
result1.s_result()

# Student record using Polymorphism
print("Using Polymorphism")
class name:
    def s_record(self):
        print("Name: Vishnu")
class age:
    def s_record(self):
        print("Age: 23")
class marks:
    def s_record(self):
        print("Marks: 85")
class result:
    def s_record(self):
        print("Result: Pass")

Records = [name(), age(), marks(), result()]
for record in Records:
    record.s_record()

# Using Abstraction
print("Using Abstraction")

from abc import ABC, abstractmethod

class Record(ABC):
    @abstractmethod
    def sr(self):
        pass

class name(Record):
    def sr(self):
        print("Name: Vishnu")

class age(Record):
    def sr(self):
        print("Age: 23")

class marks(Record):
    def sr(self):
        print("Marks: 85")

class result(Record):
    def sr(self):
        print("Result: Pass")


name1 = name()
name1.sr()

age1 = age()
age1.sr()

marks1 = marks()
marks1.sr()

result1 = result()
result1.sr()