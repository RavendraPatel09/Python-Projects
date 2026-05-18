students = {}
while True:
    print("1.Add 2.View 3.Exit")
    ch = input()
    if ch == "1":
        name = input("Name: ")
        marks = input("Marks: ")
        students[name] = marks
    elif ch == "2":
        print(students)
    else:
        break