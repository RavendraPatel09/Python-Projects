import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://open.er-api.com/v6/latest/USD"
        self.data = self.fetch_rates()
        self.rates = self.data.get('rates', {})
    def fetch_rates(self):
        try:
            response = requests.get(self.api_url)
            return response.json()
        except Exception:
            return {}
    def get_supported_currencies(self):
        return list(self.rates.keys())
    def convert(self, from_curr, to_curr, amount):
        if from_curr != "USD":
            amount = amount / self.rates.get(from_curr)
        
        result = amount * self.rates.get(to_curr)
        return round(result, 2)
def main():
    converter = CurrencyConverter()
    
    if not converter.rates:
        print("Error: Could not retrieve exchange rates.")
        return
    print("--- Quick Currency Converter ---")
    try:
        from_c = input("From Currency (e.g., USD): ").upper()
        to_c = input("To Currency (e.g., EUR): ").upper()
        amt = float(input("Amount: "))
        if from_c in converter.rates and to_c in converter.rates:
            converted_amt = converter.convert(from_c, to_c, amt)
            print(f"{amt} {from_c} = {converted_amt} {to_c}")
        else:
            print("Currency code not supported.")
            
    except ValueError:
        print("Please enter a valid numeric amount.")
if __name__ == "__main__":
    main()