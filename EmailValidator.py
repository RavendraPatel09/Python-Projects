import re
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"
while True:
    email = input("Enter email (or 'quit'): ")
    if email == "quit": break
    if re.match(pattern, email):
        parts = email.split("@")
        print(f"Valid! User: {parts[0]}, Domain: {parts[1]}")
    else:
        print("Invalid email address.")