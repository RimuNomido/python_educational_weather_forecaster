from geopy import Nominatim
from dotenv import load_dotenv
import requests
import os

load_dotenv()
YANDEX_URL = 'https://api.weather.yandex.ru/graphql/query'
YANDEX_ACCESS_KEY = os.environ.get('access_key')

class WeatherUtilities:
    def __init__(self, city: str):
        self.city = city
    
    def get_coords(self) -> tuple[float, float] | None:
        geolocator = Nominatim(user_agent='rimunomido')
        loc = geolocator.geocode(self.city)

        if loc is None:
            print('Город не найден. Проверьте название.')
            return None
    
        lat = loc.latitude
        lon = loc.longitude
        self.lat, self.lon = lat, lon

        return (lat, lon)

class ApiConn:
    def __init__(self, url: str, access_key: str):
        self.url = url
        self.access_key = access_key
        self.headers = {'X-Yandex-Weather-Key': self.access_key}
    
    # Возвращает словарь из нескольких подсловарей.
    def send_request(self, coords: tuple[float, float]) -> dict | None:
        query = """
        query GetWeather($lat: Float!, $lon: Float!) {
            weatherByPoint(request: { lat: $lat, lon: $lon }) {
                now {
                cloudiness
                humidity
                precType
                precStrength
                pressure
                temperature
                fahrenheit: temperature(unit: FAHRENHEIT)
                windSpeed
                windDirection
                }
            }
        }
        """
        variables = {
            "lat": coords[0],
            "lon": coords[1]
        }

        try:
            response = requests.post(self.url, headers=self.headers, json={'query': query, 'variables': variables}, timeout=5)
            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Ошибка сети: {e}')
            return None
        except ValueError as e:
            print(f'Ошибка парсинга JSON: {e}')
            return None