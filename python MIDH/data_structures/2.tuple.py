# Tuple Methods
# Example 1

colors = ("Red", "Blue", "Green", "Orange","Red")
print(colors)
print("Count menthod in tuple: ",colors.count("Red"))
print("Index menthod in tuple: ",colors.index("Blue"))

# Example 2
Weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
WeekEnds = ("Saturday", "Sunday")

for day in Weekdays:
    print("Working day: ",day)

for day in WeekEnds:
    print("Weekends: ",day)
