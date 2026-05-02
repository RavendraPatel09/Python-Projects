subjects = []
while True:
    name = input("Subject (or 'done'): ")
    if name == "done":
        break
    mark = float(input("Mark out of 100: "))
    subjects.append((name, mark))
avg = sum(m for _, m in subjects) / len(subjects)
print(f"Average: {avg:.1f}")
if avg >= 90: print("Grade: A")
elif avg >= 75: print("Grade: B")
elif avg >= 60: print("Grade: C")
elif avg >= 45: print("Grade: D")
else: print("Grade: F")