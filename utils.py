from dataclasses import dataclass
import pymorphy3

@dataclass
class WeatherData:
    cloudiness: str
    humidity: int
    precType: str
    precStrength: str
    pressure: int
    temperature: int
    fahrenheit: int
    windSpeed: float
    windDirection: str

class Parser:
    def __init__(self, response: dict, city: str):
        self.response = response
        self.city = city
    
    def parse_json(self) -> WeatherData:
        json = self.response
        try:
            weather = json['data']['weatherByPoint']['now']
            return WeatherData(**weather)
        except (KeyError, TypeError):
            return None
    
    def parse_city_name(self):
        morph = pymorphy3.MorphAnalyzer()
        parsed_word = morph.parse(self.city)[0]
        declined_word = parsed_word.inflect({'loct'})
        if declined_word is None:
            return self.city
        city = declined_word.word.capitalize()
        return city

def display_all_data(data: WeatherData, city: str) -> None:
    width = 51
    print(f'Погода в {city}'.center(width, "*"))
    print(f"Облачность: {data.cloudiness}")
    print(f"Влажность: {data.humidity}%")
    print(f"Тип осадков: {data.precType}")
    print(f"Интенсивность осадков: {data.precStrength}")
    print(f"Атмосферное давление: {data.pressure} мм рт. ст.")
    print(f"Температура: {data.temperature} °C")
    print(f"Температура по Фаренгейту: {data.fahrenheit} °F")
    print(f"Скорость ветра: {data.windSpeed} м/с")
    print(f"Направление ветра: {data.windDirection}")
    print('*' * width)
