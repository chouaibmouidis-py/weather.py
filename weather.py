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
        # CORRECTED: On cherche le NOM de la variable dans le .env, pas la valeur
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError(
                "API_KEY non trouvée dans le fichier .env. Vérifiez votre fichier .env")

    def get_current_weather(self, city="Casablanca"):
        """
        Récupère les données météorologiques pour une ville donnée.
        Retourne le JSON de la réponse ou None en cas d'erreur.
        """
        url = f'https://api.openweathermap.org/data/2.5/weather?appid={self.api_key}&q={city}&units=metric'

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Lève une erreur si la requête a échoué (ex: 404)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(
                f"Erreur lors de la récupération des données pour {city} : {e}")
            return None


# ==========================================
# BLOC DE TEST
# ==========================================
if __name__ == "__main__":
    app = WeatherApp()

    # Liste de villes
    cities = ["Casablanca", "Paris", "Tokyo", "New York"]

    print("--- 🌤️  WORLD WEATHER MONITOR 🌤️ ---")
    print("=" * 40)

    for city in cities:
        data = app.get_current_weather(city)
        if data:
            print(f"📍 City: {data['name']}")
            print(f"🌡️  Temp: {data['main']['temp']}°C")
            print(f"☁️  Condition: {data['weather'][0]['description']}")
            print("-" * 20)
        else:
            print(f"❌ Could not retrieve data for {city}")
            print("-" * 20)

    print("=" * 40)
