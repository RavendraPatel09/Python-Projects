import difflib
dictionary = [
    "python","programming","computer","function","variable","integer",
    "boolean","string","list","dictionary","loop","class","object",
    "module","import","print","input","return","define","library"
]
text = input("Enter a sentence to spell check:")
words = text.split()
for word in words:
    clean = word.strip(".,!?").lower()
    if clean not in dictionary:
        suggestions = difflib.get_close_matches(clean, dictionary, n=3)
        if suggestions:
            print(f"'{word}' -> did you mean: {', '.join(suggestions)}?")
        else:
            print(f"'{word}' -> no suggestions found")