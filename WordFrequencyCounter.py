import re
from collections import Counter
def count_words(path):
    with open(path, "r") as f:
        text = f.read().lower()
    words = re.findall(r"[a-z']+", text)
    return Counter(words)
def main():
    path = input("Text file path: ")
    counts = count_words(path)
    top_n = int(input("Show top how many words: "))
    for word, freq in counts.most_common(top_n):
        print(f"{word}: {freq}")
if __name__ == "__main__":
    main()
