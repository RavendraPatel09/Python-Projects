mood = input("How are you feeling today? ")
with open("mood.txt", "a") as f:
    f.write(mood + "\n")

print("Saved your mood ")