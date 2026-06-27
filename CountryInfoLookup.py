import requests
def get_country_info(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()[0]
def main():
    name = input("Country name: ")
    info = get_country_info(name)
    if not info:
        print("Country not found")
        return
    print(f"Name: {info['name']['common']}")
    print(f"Capital: {info.get('capital', ['N/A'])[0]}")
    print(f"Population: {info['population']:,}")
    print(f"Region: {info['region']}")
    currencies = list(info.get("currencies", {}).keys())
    print(f"Currencies: {', '.join(currencies)}")
if __name__ == "__main__":
    main()
