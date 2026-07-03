import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(url, params=params)
    data = response.json()
    if "results" not in data:
        return None
    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    response = requests.get(url, params=params)
    return response.json()["current_weather"]

def main():
    city = input("City name: ")
    coords = get_coordinates(city)
    if not coords:
        print("City not found")
        return
    lat, lon, name = coords
    weather = get_weather(lat, lon)
    print(f"Weather in {name}:")
    print(f"Temperature: {weather['temperature']}C")
    print(f"Wind speed: {weather['windspeed']} km/h")

if __name__ == "__main__":
    main()
