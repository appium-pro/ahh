from appium import webdriver
from conftest import MakeDriver
from pages import CityListPage


class TestIOSWeather(object):

    CITY_NAME = 'Phoenix'

    def test_weather(self: 'TestIOSWeather', make_driver: MakeDriver) -> None:
        driver: webdriver.Remote = make_driver('weather')
        # TODO ensure that test always starts on city list view
        city_page = CityListPage.instance(driver)
        city_page.add_city(self.CITY_NAME[:-1], self.CITY_NAME)
        weather_page = city_page.open_weather_for_city(self.CITY_NAME)
        hourly_weather = weather_page.get_hourly_weather()
        # TODO assert something in hourly weather
        daily_weather = weather_page.get_daily_weather()
        # TODO assert something about daily weather
        sunrise = weather_page.get_sunrise()
        # TODO assert something about sunrise
        city_page = weather_page.open_city_list()
        city_page.remove_city(self.CITY_NAME)
