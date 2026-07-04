from weather_data import WeatherData


def main():
    """
    creates object and fetches weather info.
    """

    weather = WeatherData(
        latitude=27.9659,
        longitude=-82.4389,
        month=2,
        day=23,
        year=2025
    )

    # fetch weather data
    weather.get_temperature_data()
    weather.get_wind_data()
    weather.get_precipitation_data()

    # fetch temperature data
    print("TEMPERATURE STATISTICS")
    print("----------------------")
    print(f"Average Temperature: {weather.avg_temperature:.2f}°F")
    print(f"Minimum Temperature: {weather.min_temperature:.2f}°F")
    print(f"Maximum Temperature: {weather.max_temperature:.2f}°F")

    # fetch wind data
    print("\nWIND STATISTICS")
    print("----------------")
    print(f"Average Wind Speed: {weather.avg_wind_speed:.2f} mph")
    print(f"Minimum Wind Speed: {weather.min_wind_speed:.2f} mph")
    print(f"Maximum Wind Speed: {weather.max_wind_speed:.2f} mph")

    # fetch precipitation data
    print("\nPRECIPITATION STATISTICS")
    print("------------------------")
    print(f"Total Precipitation: {weather.sum_precipitation:.2f} in")
    print(f"Minimum Precipitation: {weather.min_precipitation:.2f} in")
    print(f"Maximum Precipitation: {weather.max_precipitation:.2f} in")


if __name__ == "__main__":
    main()
