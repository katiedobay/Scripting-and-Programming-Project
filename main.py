from weather_data import WeatherData
from database import create_database
from database import save_weather_data
from database import get_weather_data


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

    weather_record = get_weather_data(engine)

    print("\nWEATHER RECORD")
    print("=" * 40)

    print(f"Latitude: {weather_record.latitude}")
    print(f"Longitude: {weather_record.longitude}")

    print(f"Month: {weather_record.month}")
    print(f"Day: {weather_record.day}")
    print(f"Year: {weather_record.year}")

    print("\nTemperature Statistics")
    print("-" * 25)
    print(f"Average Temperature: {weather_record.avg_temperature:.2f}")
    print(f"Minimum Temperature: {weather_record.min_temperature:.2f}")
    print(f"Maximum Temperature: {weather_record.max_temperature:.2f}")

    print("\nWind Statistics")
    print("-" * 25)
    print(f"Average Wind Speed: {weather_record.avg_wind_speed:.2f}")
    print(f"Minimum Wind Speed: {weather_record.min_wind_speed:.2f}")
    print(f"Maximum Wind Speed: {weather_record.max_wind_speed:.2f}")

    print("\nPrecipitation Statistics")
    print("-" * 25)
    print(f"Total Precipitation: {weather_record.sum_precipitation:.2f}")
    print(f"Minimum Precipitation: {weather_record.min_precipitation:.2f}")
    print(f"Maximum Precipitation: {weather_record.max_precipitation:.2f}")


if __name__ == "__main__":
    main()