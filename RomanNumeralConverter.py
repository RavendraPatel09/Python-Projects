VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

ROMAN_MAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def int_to_roman(num):
    result = ""
    for value, symbol in VALUES:
        while num >= value:
            result += symbol
            num -= value
    return result

def roman_to_int(roman):
    total = 0
    prev = 0
    for char in reversed(roman.upper()):
        value = ROMAN_MAP.get(char, 0)
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total
def main():
    mode = input("Convert to roman or to int (r/i): ").lower()
    if mode == "r":
        num = int(input("Number: "))
        print(int_to_roman(num))
    elif mode == "i":
        roman = input("Roman numeral: ")
        print(roman_to_int(roman))
    else:
        print("Invalid mode")
if __name__ == "__main__":
    main()
