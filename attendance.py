held = int(input("Enter total classes held: "))
attendance = int(input("Enter classes attended: "))

percentage = (attendance/ held) * 100
print("Attendance= ", percentage, "%")
if percentage >= 75:
    print("Eligible for exams")
else:
    print("Not eligible for exams")