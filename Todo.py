import json
import os
import sys
from datetime import datetime
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")
def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
def add_task(text):
    tasks = load_tasks()
    task = {
        "id": (tasks[-1]["id"] + 1) if tasks else 1,
        "text": text,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{task['id']}: {text}")
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python todo.py add \"Your task\"")
        return
    print("\nYour Tasks:")
    print("-" * 40)
    for task in tasks:
        status = "[x]" if task["done"] else "[ ]"
        print(f"{status} #{task['id']}: {task['text']} (added {task['created']})")
    print("-" * 40)
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Marked task #{task_id} as done.")
            return
    print(f"Task #{task_id} not found.")
def remove_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task #{task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Removed task #{task_id}.")
def print_help():
    print(__doc__)
def main():
    args = sys.argv[1:]
    if not args:
        print_help()
        return
    command = args[0].lower()
    if command == "add":
        if len(args) < 2:
            print("Please provide task text. Example: python todo.py add \"Buy milk\"")
            return
        add_task(" ".join(args[1:]))
    elif command == "list":
        list_tasks()
    elif command == "done":
        if len(args) < 2 or not args[1].isdigit():
            print("Please provide a valid task number. Example: python todo.py done 1")
            return
        complete_task(int(args[1]))
    elif command == "remove":
        if len(args) < 2 or not args[1].isdigit():
            print("Please provide a valid task number. Example: python todo.py remove 1")
            return
        remove_task(int(args[1]))
    elif command in ("help", "-h", "--help"):
        print_help()
    else:
        print(f"Unknown command: {command}")
        print_help()
if __name__ == "__main__":
    main()