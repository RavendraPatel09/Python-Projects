# Simple Library Management System

library = []

def add_book():# Function to add a book to the library
    book_id = input("Enter Book ID: ")# Get book details from user
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "issued": False
    }

    library.append(book)
    print("Book added successfully!\n")


def show_books():
    if not library:
        print("No books available\n")
        return

    print("\n📚 Library Books:")
    for book in library:
        status = "Issued" if book["issued"] else "Available"
        print(f'ID: {book["id"]}, Name: {book["name"]}, Author: {book["author"]}, Status: {status}')
    print()


def issue_book():# Function to issue a book
    book_id = input("Enter Book ID to issue: ")

    for book in library:
        if book["id"] == book_id:
            if not book["issued"]:
                book["issued"] = True
                print(" Book issued successfully!\n")
                return
            else:
                print(" Book already issued\n")
                return

    print("Book not found\n")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in library:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                print("📗 Book returned successfully!\n")
                return
            else:
                print("Book was not issued\n")
                return

    print(" Book not found\n")


while True:
    print("====== Library Management System ======")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("👋 Exiting Library System. Thank you!")
        break
    else:
        print(" Invalid choice\n")