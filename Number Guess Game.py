import random

num = random.randint(1, 50)

while True:
    guess = int(input("Guess number: "))
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("Correct!")
        break