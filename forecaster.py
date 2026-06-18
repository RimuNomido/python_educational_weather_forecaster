import requests
import os
from dotenv import load_dotenv
from geopy import Nominatim

load_dotenv()

class WeatherForecaster:
    def __init__(self, city = 'Moscow'):
        self.url = 'https://api.weather.yandex.ru/graphql/query'
        self.access_key = os.environ.get('access_key')
        self.city = city
    
    def get_coords(self):
        geolocator = Nominatim(user_agent='rimunomido')
        loc = geolocator.geocode(self.city)
        lat = loc.latitude
        lon = loc.longitude
        self.lat, self.lon = lat, lon

        return (lat, lon)
        
    def get_weather(self):
        headers = {'X-Yandex-Weather-Key': self.access_key}
        coords = self.get_coords()
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
        response = requests.post(self.url, headers=headers, json={'query': query, 'variables': variables})

        return response.json()