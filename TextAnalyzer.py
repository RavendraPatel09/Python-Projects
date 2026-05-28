import re
def analyze(text):
    text = text.strip()
    sentences = len(re.findall(r'[.!?]+', text)) or 1
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    word_count = len(words)
    char_count = len(text.replace(" ", ""))
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
    longest = max(words, key=len) if words else "N/A"
    print(f"\n--- Text Analysis ---")
    print(f"Characters (no spaces): {char_count}")
    print(f"Total Words            : {word_count}")
    print(f"Sentences              : {sentences}")
    print(f"Unique Words           : {len(freq)}")
    print(f"Longest Word           : {longest}")
    print(f"Top 5 Frequent Words   :")
    for word, count in top5:
        print(f"  '{word}' appears {count} time(s)")
print("Paste your text below (press Enter twice to submit):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
analyze(" ".join(lines))