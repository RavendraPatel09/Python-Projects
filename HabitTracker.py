import json
import os
from datetime import datetime, timedelta
FILE = "habits.json"
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
def mark_done(data):
    habit = input("Habit name: ")
    today = datetime.now().strftime("%Y-%m-%d")
    if habit not in data:
        data[habit] = []
    if today not in data[habit]:
        data[habit].append(today)
        save_data(data)
        print("Marked done for today")
    else:
        print("Already marked today")
def calc_streak(dates):
    if not dates:
        return 0
    parsed = sorted([datetime.strptime(d, "%Y-%m-%d") for d in dates], reverse=True)
    streak = 1
    for i in range(len(parsed) - 1):
        if (parsed[i] - parsed[i + 1]).days == 1:
            streak += 1
        else:
            break
    return streak
def show_streaks(data):
    if not data:
        print("No habits tracked yet")
    for habit, dates in data.items():
        print(f"{habit}: streak {calc_streak(dates)} days, total {len(dates)} days")
def main():
    data = load_data()
    while True:
        print("1.Mark done 2.Show streaks 3.Exit")
        ch = input()
        if ch == "1":
            mark_done(data)
        elif ch == "2":
            show_streaks(data)
        elif ch == "3":
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
