data = {}
while True:
    print("1.Save 2.View 3.Exit")
    ch = input()
    if ch == "1":
        site = input("Site: ")
        pwd = input("Password: ")
        data[site] = pwd
    elif ch == "2":
        print(data)
    else:
        break