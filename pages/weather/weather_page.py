from pages import BasePage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages import CityListPage


class WeatherPage(BasePage):

    def get_hourly_weather(self: 'WeatherPage') -> None:
        pass

    def get_daily_weather(self: 'WeatherPage') -> None:
        pass

    def get_sunrise(self: 'WeatherPage') -> None:
        pass

    def open_city_list(self: 'WeatherPage') -> 'CityListPage':
        from pages import CityListPage
        return CityListPage.instance(self.driver)


class WeatherPageIOS(WeatherPage):
    pass
