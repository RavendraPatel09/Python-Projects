import time
text = "Python is a powerful programming language"
input("Press Enter to start...")
start = time.time()
typed = input("Type this:\n" + text + "\n")
end = time.time()
time_taken = end - start
speed = len(typed.split()) / (time_taken / 60)
print("WPM:", int(speed))