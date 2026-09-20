import requests
import os
from dotenv import load_dotenv

# On charge les variables d'environnement (API KEY)
load_dotenv()


class WeatherApp:
    """
    Application permettant de récupérer la météo actuelle d'une ville 
    via l'API OpenWeatherMap.
    """

    def __init__(self):
        # On récupère la clé API depuis le fichier .env
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API_KEY non trouvée dans le fichier .env")

    def get_current_weather(self, city="Casablanca"):
        """
        Récupère les données météorologiques pour une ville donnée.
        Retourne le JSON de la réponse ou None en cas d'erreur.
        """
        url = f'https://api.openweathermap.org/data/2.5/weather?appid={self.api_key}&q={city}&units=metric'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Lève une erreur si la requête a échoué (ex: 404)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération des données : {e}")
            return None


if __name__ == "__main__":
    app = WeatherApp()
    city = input("\nPlease enter a city name: ")
    data = app.get_current_weather(city)

    if data:
        print(f"\nWeather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description']}")
