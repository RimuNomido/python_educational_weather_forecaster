from forecaster import WeatherForecaster
from utils import Parser, Displayer

def main():
    city = input('Введите город: ')
    forecaster = WeatherForecaster(city)
    parser = Parser(forecaster.get_weather())
    displayer = Displayer(parser.parse_json(), city)
    displayer.display_weather()

if __name__ == '__main__':
    main()