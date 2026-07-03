import requests
def get_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    return response.json()["message"]
def get_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    return response.json()[0]["url"]
def main():
    choice = input("Dog or cat? (d/c): ").lower()
    if choice == "d":
        print(get_dog_image())
    elif choice == "c":
        print(get_cat_image())
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
