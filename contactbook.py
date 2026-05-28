contacts = {}
def add():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added.")
def view():
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"{name} | Phone: {info['phone']} | Email: {info['email']}")
def search():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name} | Phone: {contacts[name]['phone']} | Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")
def update():
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    contacts[name]["phone"] = input("New Phone: ").strip()
    contacts[name]["email"] = input("New Email: ").strip()
    print("Contact updated.")
def delete():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")
while True:
    print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
    choice = input("Choose: ").strip()
    if choice == "1": add()
    elif choice == "2": view()
    elif choice == "3": search()
    elif choice == "4": update()
    elif choice == "5": delete()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")