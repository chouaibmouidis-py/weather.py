import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherApp:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")

    def get_current_weather(self, city="Casablanca"):
        if not city or not city.strip():
            city = "Casablanca"

        if not self.api_key:
            return {"cod": "401", "message": "Invalid API key"}

        url = f'https://api.openweathermap.org/data/2.5/weather?appid={self.api_key}&q={city}&units=metric'

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Lève une erreur pour les codes 4xx et 5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"cod": "500", "message": str(e)}


if __name__ == "__main__":
    app = WeatherApp()
    city = input("\nPlease enter a city name: ")
    data = app.get_current_weather(city)

    if data and 'main' in data:
        print(f"\nWeather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description']}")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")
