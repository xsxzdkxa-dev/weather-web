import requests

def get_weather(city: str) -> dict | None:
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            current = data["current_condition"][0]
            return {
                "city": city,
                "temp": current["temp_C"],
                "feels_like": current["FeelsLikeC"],
                "humidity": current["humidity"],
                "wind": current["windspeedKmph"],
            }
        else:
            return None
    except (requests.RequestException, KeyError, IndexError):
        return None

if __name__ == "__main__":
    print(get_weather("Lviv"))