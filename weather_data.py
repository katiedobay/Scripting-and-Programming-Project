class WeatherData:
    """
    stores weather data Ybor City on Feb 23rd from years 2021-2025
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
