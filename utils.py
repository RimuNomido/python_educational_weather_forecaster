from types import SimpleNamespace

class Parser:
    def __init__(self, response):
        self.response = response
    
    def parse_json(self):
        json = self.response
        weather = json['data']['weatherByPoint']['now']
        data = SimpleNamespace(**weather)

        return data
    
class Displayer:
    def __init__(self, data, city):
        self.city = city
        self.temp = data.temperature
        self.fahr = data.fahrenheit
        self.wind_speed = data.windSpeed
        self.wind_direct = data.windDirection
    
    def display_weather(self):
        width = 51
        print(f'Погода в {self.city}'.center(width, "*"))
        print(f'Температура (Цельсий): {self.temp}')
        print(f'Температура (Фаренгейты): {self.fahr}')
        print(f'Скорость ветра: {self.wind_speed}')
        print(f'Направление ветра: {self.wind_direct}')
        print('*' * width)