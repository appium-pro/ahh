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
        import time; time.sleep(2)
        weather_page = city_page.open_weather_for_city(self.CITY_NAME)
        time.sleep(2)
        hourly_weather = weather_page.get_hourly_weather()
        assert hourly_weather[2]['weather'] in ['Partly sunny', 'Partly cloudy', 'Sunny']
        assert hourly_weather[2]['temp'] in range(30, 45)
        daily_weather = weather_page.get_daily_weather()
        assert daily_weather[2]['weather'] in ['Partly sunny', 'Partly cloudy', 'Sunny']
        assert daily_weather[2]['high_temp'] in range(30, 45)
        assert daily_weather[2]['low_temp'] in range(20, 35)
        city_page = weather_page.open_city_list()
        # TODO fix remove city
        city_page.remove_city(self.CITY_NAME)
