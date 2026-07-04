from weather_data import WeatherData

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

print("Temperature Statistics")
print("----------------------")
print("Average:", weather.avg_temperature)
print("Minimum:", weather.min_temperature)
print("Maximum:", weather.max_temperature)

print("\nWind Statistics")
print("----------------")
print("Average:", weather.avg_wind_speed)
print("Minimum:", weather.min_wind_speed)
print("Maximum:", weather.max_wind_speed)

print("\nPrecipitation Statistics")
print("-------------------------")
print("Total:", weather.sum_precipitation)
print("Minimum:", weather.min_precipitation)
print("Maximum:", weather.max_precipitation)
