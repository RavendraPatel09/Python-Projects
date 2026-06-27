import re
from collections import Counter

def analyze_log(path):
    levels = Counter()
    timestamps = []
    pattern = re.compile(r"\[(.*?)\]\s+(ERROR|WARNING|INFO)")
    with open(path, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                timestamps.append(match.group(1))
                levels[match.group(2)] += 1
    return levels, timestamps

def main():
    path = input("Log file path: ")
    levels, timestamps = analyze_log(path)
    print("Level counts:")
    for level, count in levels.items():
        print(f"{level}: {count}")
    if timestamps:
        print(f"First entry: {timestamps[0]}")
        print(f"Last entry: {timestamps[-1]}")

if __name__ == "__main__":
    main()
