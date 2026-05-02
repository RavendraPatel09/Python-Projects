import random
words = ["python", "framework", "computer", "keyboard"]
word = random.choice(words)
guessed = []
lives = 6
while lives > 0:
    display = " ".join(c if c in guessed else "_" for c in word)
    print(display)
    if "_" not in display:
        print("You won!"); break
    letter = input("Guess a letter: ").lower()
    if letter in word:
        guessed.append(letter)
    else:
        lives -= 1
        print(f"Wrong! {lives} lives left")
else:
    print(f"Game over! Word was: {word}")