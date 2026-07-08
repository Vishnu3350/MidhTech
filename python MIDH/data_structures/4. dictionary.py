# Example  -> Student marks update and delete

S_record = {"name": "Vishnu", "marks": "90"}
S_record["marks"] = 92
S_record["Grade"] = "S"
print("Student Record: ",S_record)


# Example 2 -> Employee Details Update and insert 
E_details = {"id":"MDT063","name" : "Vishnu", "dept" : "IT", "salary" : 50000}

print("Employee Details", E_details)

print("Employee name: ",E_details["name"])
E_details["city"] = "Hyderabad"

print("After adding city name: ",E_details)
E_details["salary"] = "30000"
print("After Updating salary: ",E_details)


# Example 3 -> Product Details

P_details = {"id": "P201", "name": "Laptop", "brand": "Lenovo", "price": 44000}

print("Product Details:", P_details)

print("Product Name:", P_details["name"])

P_details["color"] = "Black"
print("After adding color:", P_details)

P_details["price"] = 48000
print("After updating price:", P_details)