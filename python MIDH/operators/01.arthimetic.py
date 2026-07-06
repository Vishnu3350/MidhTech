# Arthmetice Operators

s1 = int(input("Enter marks in TELUGU : "))
s2 = int(input("Enter marks in HINDI : "))
s3 = int(input("Enter marks in ENGLISH : "))
s4 = int(input("Enter marks in MATHS : "))
s5 = int(input("Enter marks in SCIENCE : "))
s6 = int(input("Enter marks in SOCIAL : "))

Total = s1 + s2 + s3 + s4 + s5 + s6
print("Total Marks: " ,Total)
Avg_of_total = s1 + s2 + s3 + s4 + s5 + s6 / 6  
print("Average is: ", Avg_of_total)
print("Percentage is: ",Total/600 * 100)


# Example : There are 30 students in a college. In that 20 students were paid the college fee. How much did the students paid to college ?

Students_Paid_count = 20
college_fee = 100
print ("No.of students paid fee to college: ", Students_Paid_count * college_fee)