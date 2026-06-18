from forecaster import WeatherUtilities, ApiConn, YANDEX_ACCESS_KEY, YANDEX_URL
from utils import Parser, Displayer
from typing import Annotated
import typer



def main(city: Annotated[str, typer.Option('-c', '--city', help='Город для прогноза')] = 'Сочи') -> None:
    utility = WeatherUtilities(city)
    coords = utility.get_coords()
    if coords is None:
        print('Не удалось получить координаты.')
        return 
    conn = ApiConn(YANDEX_URL, YANDEX_ACCESS_KEY)
    weather_data = conn.send_request(coords)

    if weather_data is None:
        print('Не удалось получить погоду.')
        return

    parser = Parser(weather_data, city)
    parsed_city = parser.parse_city_name()
    parsed_data = parser.parse_json()

    if parsed_data is None:
        print('Ошибка обработки данных.')
        return

    displayer = Displayer(parsed_data, parsed_city)
    displayer.display_weather()

if __name__ == '__main__':
    typer.run(main)