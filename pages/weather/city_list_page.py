from pages import BasePage, WeatherPage


class CityListPage(BasePage):

    def open_weather_for_city(self: 'CityListPage', name: str) -> WeatherPage:
        return WeatherPage.instance(self.driver)

    def add_city(self: 'CityListPage', search_text: str, found_text: str) -> None:
        pass

    def remove_city(self: 'CityListPage', name: str) -> None:
        pass


class CityListPageIOS(CityListPage):
    pass
