import random
scores = {"easy": 0, "medium": 0, "hard": 0}
def play():
    print("\nChoose Difficulty: 1.Easy(1-50)  2.Medium(1-100)  3.Hard(1-200)")
    ch = input("Choice: ").strip()
    if ch == "1": level, high, tries = "easy", 50, 10
    elif ch == "2": level, high, tries = "medium", 100, 7
    elif ch == "3": level, high, tries = "hard", 200, 5
    else:
        print("Invalid choice.")
        return
    secret = random.randint(1, high)
    print(f"\nGuess the number between 1 and {high}. You have {tries} attempts.")
    for attempt in range(1, tries + 1):
        guess = int(input(f"Attempt {attempt}/{tries}: "))
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            points = (tries - attempt + 1) * 10
            scores[level] += points
            print(f"Correct! You earned {points} points. Total [{level}]: {scores[level]}")
            return
    print(f"Out of attempts! The number was {secret}.")
while True:
    print("\n1.Play  2.View Scores  3.Exit")
    choice = input("Choose: ").strip()
    if choice == "1": play()
    elif choice == "2":
        for lvl, sc in scores.items():
            print(f"{lvl.capitalize()}: {sc} points")
    elif choice == "3":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice.")