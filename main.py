from weather_data import WeatherData
from database import create_database
from database import save_weather_data


def main():

    weather = WeatherData(
        latitude=27.9659,
        longitude=-82.4389,
        month=2,
        day=23,
        year=2025
    )

    weather.get_temperature_data()
    weather.get_wind_data()
    weather.get_precipitation_data()

    engine = create_database()

    save_weather_data(engine, weather)

    print("Weather data saved successfully.")


if __name__ == "__main__":
    main()