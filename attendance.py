held = int(input("Enter total classes held: "))
attendance = int(input("Enter classes attended: "))

percentage = (attendance/ held) * 100
print("Attendance= ", percentage, "%")