def encode(text):
    if not text:
        return ""
    result = []
    count = 1
    prev = text[0]
    for char in text[1:]:
        if char == prev:
            count += 1
        else:
            result.append(f"{prev}{count}")
            prev = char
            count = 1
    result.append(f"{prev}{count}")
    return "".join(result)

def decode(encoded):
    result = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        num = ""
        while i < len(encoded) and encoded[i].isdigit():
            num += encoded[i]
            i += 1
        result.append(char * int(num))
    return "".join(result)

def main():
    mode = input("Encode or decode (e/d): ").lower()
    text = input("Text: ")
    if mode == "e":
        print(encode(text))
    elif mode == "d":
        print(decode(text))
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()
