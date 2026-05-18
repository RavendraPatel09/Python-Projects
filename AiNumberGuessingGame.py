print("Think of a number between 1 and 100")
low = 1
high = 100
while True:
    mid = (low + high) // 2
    print(f"AI guesses: {mid}")
    choice = input("Enter h (high), l (low), c (correct): ")
    if choice == 'c':
        print("AI guessed correctly!")
        break
    elif choice == 'h':
        high = mid - 1
    elif choice == 'l':
        low = mid + 1