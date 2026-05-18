expenses = []
while True:
    action = input("add / total / list / quit: ")
    if action == "add":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append((name, amount))
    elif action == "total":
        print(f"Total: {sum(a for _, a in expenses):.2f}")
    elif action == "list":
        for name, amount in expenses:
            print(f"{name}: {amount:.2f}")
    elif action == "quit":
        break