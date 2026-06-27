import requests

def get_price(coin_id, currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": currency}
    response = requests.get(url, params=params)
    data = response.json()
    if coin_id not in data:
        return None
    return data[coin_id][currency]

def main():
    coin = input("Coin id (e.g. bitcoin, ethereum): ").lower()
    currency = input("Currency (e.g. usd, inr): ").lower() or "usd"
    price = get_price(coin, currency)
    if price is None:
        print("Coin not found")
        return
    print(f"{coin.capitalize()} price: {price} {currency.upper()}")

if __name__ == "__main__":
    main()
