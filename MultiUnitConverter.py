LENGTH_TO_METERS = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "inch": 0.0254, "foot": 0.3048, "mile": 1609.34}
WEIGHT_TO_GRAMS = {"mg": 0.001, "g": 1, "kg": 1000, "lb": 453.592, "oz": 28.3495}

def convert_length(value, from_unit, to_unit):
    meters = value * LENGTH_TO_METERS[from_unit]
    return meters / LENGTH_TO_METERS[to_unit]

def convert_weight(value, from_unit, to_unit):
    grams = value * WEIGHT_TO_GRAMS[from_unit]
    return grams / WEIGHT_TO_GRAMS[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15
    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15

def main():
    print("1.Length 2.Weight 3.Temperature")
    category = input()
    value = float(input("Value: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()
    if category == "1":
        result = convert_length(value, from_unit, to_unit)
    elif category == "2":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "3":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        print("Invalid category")
        return
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
