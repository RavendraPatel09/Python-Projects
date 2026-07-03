import time
import sys
def show_progress(total, delay):
    bar_length = 30
    for current in range(total + 1):
        percent = current / total
        filled = int(bar_length * percent)
        bar = "#" * filled + "-" * (bar_length - filled)
        sys.stdout.write(f"\r[{bar}] {percent*100:.0f}%")
        sys.stdout.flush()
        time.sleep(delay)
    print()
def main():
    total = int(input("Number of steps: "))
    delay = float(input("Delay per step in seconds: "))
    show_progress(total, delay)
    print("Done")
if __name__ == "__main__":
    main()
