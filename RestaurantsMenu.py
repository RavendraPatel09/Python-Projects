# Simple Restaurant Menu Program

print("🍴 Welcome to Samarth's Restaurant 🍴")
print("------------ MENU ------------")
print("1. Pizza     - ₹150")
print("2. Burger    - ₹100")
print("3. Pasta     - ₹120")
print("4. Cold Drink- ₹50")
print("------------------------------")

choice = int(input("Enter the item number you want to order: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    price = 150
    item = "Pizza"
elif choice == 2:
    price = 100
    item = "Burger"
elif choice == 3:
    price = 120
    item = "Pasta"
elif choice == 4:
    price = 50
    item = "Cold Drink"
else:
    print("Invalid choice")
    price = 0
    item = ""

total = price * quantity

if price > 0:
    print("\n------ BILL ------")
    print("Item:", item)
    print("Quantity:", quantity)
    print("Total Amount: ₹", total)
    print("Thank you! Visit again ")
