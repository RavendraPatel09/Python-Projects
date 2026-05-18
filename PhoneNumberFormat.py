def format_phone(number):
    digits = "".join(filter(str.isdigit, number))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11:
        return f"+{digits[0]} ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return "Invalid number"
while True:
    number = input("Enter phone number (or 'quit'): ")
    if number == "quit":
        break
    print("Formatted:", format_phone(number))