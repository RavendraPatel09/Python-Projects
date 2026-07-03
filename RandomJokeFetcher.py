import requests

def get_joke(category="Any"):
    url = f"https://v2.jokeapi.dev/joke/{category}"
    response = requests.get(url)
    data = response.json()
    if data["type"] == "single":
        return data["joke"]
    return f"{data['setup']}\n{data['delivery']}"

def main():
    category = input("Category (Programming/Pun/Any): ") or "Any"
    joke = get_joke(category)
    print(joke)

if __name__ == "__main__":
    main()
