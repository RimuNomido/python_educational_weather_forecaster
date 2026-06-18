from forecaster import WeatherForecaster
from utils import Parser, Displayer
from typing import Annotated
import typer

def main(city: Annotated[str, typer.Option('-c', '--city', help='Город для прогноза')] = 'Москва') -> None:
    forecaster = WeatherForecaster(city)
    parser = Parser(forecaster.get_weather(), city)
    parsed_city = parser.parse_city_name()
    displayer = Displayer(parser.parse_json(), parsed_city)
    displayer.display_weather()

if __name__ == '__main__':
    typer.run(main)