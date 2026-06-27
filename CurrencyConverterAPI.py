import requests

def get_rate(base, target):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target]

def main():
    base = input("From currency (e.g. USD): ").upper()
    target = input("To currency (e.g. EUR): ").upper()
    amount = float(input("Amount: "))
    rate = get_rate(base, target)
    converted = amount * rate
    print(f"{amount} {base} = {converted:.2f} {target}")

if __name__ == "__main__":
    main()
