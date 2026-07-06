import unittest

from weather_data import WeatherData


class TestWeatherData(unittest.TestCase):

    def setUp(self):
        self.weather = WeatherData(
            latitude=27.9659,
            longitude=-82.4389,
            month=2,
            day=23,
            year=2025
        )

    def test_latitude(self):
        self.assertEqual(self.weather.latitude, 27.9659)

    def test_longitude(self):
        self.assertEqual(self.weather.longitude, -82.4389)

    def test_month(self):
        self.assertEqual(self.weather.month, 2)


if __name__ == "__main__":
    unittest.main()
