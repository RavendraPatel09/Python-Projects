from collections import Counter

def clean_text(text):
    return "".join(c.lower() for c in text if c.isalnum())

def is_palindrome_permutation(text):
    cleaned = clean_text(text)
    counts = Counter(cleaned)
    odd_count = sum(1 for v in counts.values() if v % 2 != 0)
    return odd_count <= 1

def main():
    text = input("Enter text: ")
    if is_palindrome_permutation(text):
        print("Can be rearranged into a palindrome")
    else:
        print("Cannot be rearranged into a palindrome")

if __name__ == "__main__":
    main()
