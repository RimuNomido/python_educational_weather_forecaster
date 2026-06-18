from types import SimpleNamespace
import pymorphy3

class Parser:
    def __init__(self, response: dict, city: str):
        self.response = response
        self.city = city
    
    def parse_json(self) -> SimpleNamespace:
        json = self.response
        try:
            weather = json['data']['weatherByPoint']['now']
            return SimpleNamespace(**weather)
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
    
class Displayer:
    def __init__(self, data: SimpleNamespace, city: str):
        self.city = city
        self.temp = data.temperature
        self.fahr = data.fahrenheit
        self.wind_speed = data.windSpeed
        self.wind_direct = data.windDirection
    
    def display_weather(self) -> None:
        width = 51
        print(f'Погода в {self.city}'.center(width, "*"))
        print(f'Температура (Цельсий): {self.temp}')
        print(f'Температура (Фаренгейты): {self.fahr}')
        print(f'Скорость ветра: {self.wind_speed}')
        print(f'Направление ветра: {self.wind_direct}')
        print('*' * width)