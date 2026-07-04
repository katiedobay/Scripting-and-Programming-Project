import requests
import statistics


class WeatherData:
    """
    stores weather data for Ybor City, FL on Feb 23rd from 2021-2025.
    """

    def __init__(
            self,
            latitude,
            longitude,
            month,
            day,
            year,
            avg_temperature=0.0,
            min_temperature=0.0,
            max_temperature=0.0,
            avg_wind_speed=0.0,
            min_wind_speed=0.0,
            max_wind_speed=0.0,
            sum_precipitation=0.0,
            min_precipitation=0.0,
            max_precipitation=0.0
    ):

        # city info
        self.latitude = latitude
        self.longitude = longitude

        # date
        self.month = month
        self.day = day
        self.year = year

        # temp data
        self.avg_temperature = avg_temperature
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature

        # wind data
        self.avg_wind_speed = avg_wind_speed
        self.min_wind_speed = min_wind_speed
        self.max_wind_speed = max_wind_speed

        # precipitation data
        self.sum_precipitation = sum_precipitation
        self.min_precipitation = min_precipitation
        self.max_precipitation = max_precipitation

    def get_temperature_data(self):
        """fetch mean temps for the past five years."""

        temperatures = []

        for year in range(2021, 2026):

            url = (
                f"https://archive-api.open-meteo.com/v1/archive"
                f"?latitude={self.latitude}"
                f"&longitude={self.longitude}"
                f"&start_date={year}-{self.month:02d}-{self.day:02d}"
                f"&end_date={year}-{self.month:02d}-{self.day:02d}"
                f"&daily=temperature_2m_mean"
                f"&temperature_unit=fahrenheit"
                f"&timezone=America/New_York"
            )

            response = requests.get(url)
            data = response.json()

            temperatures.append(data["daily"]["temperature_2m_mean"][0])

        self.avg_temperature = statistics.mean(temperatures)
        self.min_temperature = min(temperatures)
        self.max_temperature = max(temperatures)

    def get_wind_data(self):
        """fetch max wind speeds for the past five years."""

        wind_speeds = []

        for year in range(2021, 2026):

            url = (
                f"https://archive-api.open-meteo.com/v1/archive"
                f"?latitude={self.latitude}"
                f"&longitude={self.longitude}"
                f"&start_date={year}-{self.month:02d}-{self.day:02d}"
                f"&end_date={year}-{self.month:02d}-{self.day:02d}"
                f"&daily=wind_speed_10m_max"
                f"&wind_speed_unit=mph"
                f"&timezone=America/New_York"
            )

            response = requests.get(url)
            data = response.json()

            wind_speeds.append(data["daily"]["wind_speed_10m_max"][0])

        self.avg_wind_speed = statistics.mean(wind_speeds)
        self.min_wind_speed = min(wind_speeds)
        self.max_wind_speed = max(wind_speeds)

    def get_precipitation_data(self):
        """fetch precipitation data for the past five years."""

        precipitation = []

        for year in range(2021, 2026):

            url = (
                f"https://archive-api.open-meteo.com/v1/archive"
                f"?latitude={self.latitude}"
                f"&longitude={self.longitude}"
                f"&start_date={year}-{self.month:02d}-{self.day:02d}"
                f"&end_date={year}-{self.month:02d}-{self.day:02d}"
                f"&daily=precipitation_sum"
                f"&precipitation_unit=inch"
                f"&timezone=America/New_York"
            )

            response = requests.get(url)
            data = response.json()

            precipitation.append(data["daily"]["precipitation_sum"][0])

        self.sum_precipitation = sum(precipitation)
        self.min_precipitation = min(precipitation)
        self.max_precipitation = max(precipitation)
