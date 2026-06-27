def caesar_shift(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)
def encode(text, shift):
    return caesar_shift(text, shift)
def decode(text, shift):
    return caesar_shift(text, -shift)
def main():
    mode = input("Encode or decode (e/d): ").lower()
    text = input("Text: ")
    shift = int(input("Shift amount: "))
    if mode == "e":
        print(encode(text, shift))
    elif mode == "d":
        print(decode(text, shift))
    else:
        print("Invalid mode")
if __name__ == "__main__":
    main()
