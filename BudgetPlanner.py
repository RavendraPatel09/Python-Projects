import json
import os
from datetime import datetime
FILE = "budget.json"
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
def add_entry(data):
    category = input("Category: ")
    amount = float(input("Amount: "))
    month = datetime.now().strftime("%Y-%m")
    data.append({"category": category, "amount": amount, "month": month})
    save_data(data)
def summary_by_category(data):
    totals = {}
    for entry in data:
        totals[entry["category"]] = totals.get(entry["category"], 0) + entry["amount"]
    for category, total in totals.items():
        print(f"{category}: {total:.2f}")
def summary_by_month(data):
    totals = {}
    for entry in data:
        totals[entry["month"]] = totals.get(entry["month"], 0) + entry["amount"]
    for month, total in totals.items():
        print(f"{month}: {total:.2f}")
def main():
    data = load_data()
    while True:
        print("1.Add expense 2.By category 3.By month 4.Exit")
        ch = input()
        if ch == "1":
            add_entry(data)
        elif ch == "2":
            summary_by_category(data)
        elif ch == "3":
            summary_by_month(data)
        elif ch == "4":
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
