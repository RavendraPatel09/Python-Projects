birth = int(input("Enter birth year: "))
current = 2026
print("Your age is:", current - birth)
month = int(input("Enter birth month (1-12): "))
if month < 1 or month > 12:
    print("Invalid month")