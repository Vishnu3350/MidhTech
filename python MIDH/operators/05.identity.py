#Identity Operators. we use "is" opearator

a = [1 , 2, 3]
b = a

print ("A is B", a is b)

basket1 = ["apple", "banana", "goa"]
basket2 = ["apple", "papaya", "orange"]
basket3 = ["apple", "banana", "goa"] # In this the values are as same as basket1, but the variable stored in another memory

print ("basket1 is basket2: ", basket1 is basket2)
print ("basket2 is basket3: ", basket2 is basket3)
print ("basket3 is basket1: ", basket1 is basket3)