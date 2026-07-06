#Bitwise Operator

Read = 1
Write = 2
Execute = 5

User_Pemission = Read | Write

print("can read: ", bool(User_Pemission & Read))
print("can write: ", bool(User_Pemission & Write))
print("can execute: ", bool(User_Pemission & Execute))