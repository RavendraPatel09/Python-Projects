import json
import os

FILE = "questions.json"

def create_default_questions():
    questions = [
        {"q": "What is the capital of France?", "options": ["Berlin", "Paris", "Rome", "Madrid"], "answer": "Paris"},
        {"q": "Which language runs in a web browser?", "options": ["Java", "C", "Python", "JavaScript"], "answer": "JavaScript"},
        {"q": "What is 7 multiplied by 8?", "options": ["54", "56", "58", "64"], "answer": "56"},
        {"q": "Who wrote Romeo and Juliet?", "options": ["Dickens", "Shakespeare", "Tolstoy", "Hemingway"], "answer": "Shakespeare"},
        {"q": "What planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": "Mars"}
    ]
    with open(FILE, "w") as f:
        json.dump(questions, f, indent=2)

def load_questions():
    if not os.path.exists(FILE):
        create_default_questions()
    with open(FILE, "r") as f:
        return json.load(f)

def ask_question(item):
    print(item["q"])
    for i, opt in enumerate(item["options"]):
        print(f"{i+1}. {opt}")
    choice = input("Your answer (1-4): ")
    try:
        selected = item["options"][int(choice) - 1]
    except (ValueError, IndexError):
        return False
    return selected == item["answer"]

def run_quiz(questions):
    score = 0
    for item in questions:
        if ask_question(item):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer: {item['answer']}")
    print(f"Final score: {score}/{len(questions)}")

def main():
    questions = load_questions()
    run_quiz(questions)

if __name__ == "__main__":
    main()
