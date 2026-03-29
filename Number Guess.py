import random
number = random.randint(1, 100)
print("Welcome to the Number Guessing Game")
while True:
    guess = int(input("Enter your guess: "))
    if guess > number:
        print("Too high! Try again.")
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the number correctly 🎉")
        break