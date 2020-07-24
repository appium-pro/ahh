from pages import BasePage, WeatherPage, ScrollDirection
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from appium.webdriver.common.mobileby import MobileBy


class CityListPage(BasePage):

    ADD_CITY = (MobileBy.ACCESSIBILITY_ID, 'Add City')
    SEARCH_CITY = (By.XPATH, '//XCUIElementTypeSearchField[@name="Search"]')
    DELETE_CITY = (By.XPATH, '//XCUIElementTypeButton[@name="Delete"]')

    def _get_city_el(self: 'CityListPage', name: str) -> WebElement:
        locator = (By.XPATH, f'//*[contains(@name, "{name}")]')
        el = None
        try:
            el = self.scroll_to(locator, direction=ScrollDirection.down, max_scrolls=5)
        except Exception:
            el = self.scroll_to(locator, direction=ScrollDirection.up, max_scrolls=5)
        return el

    def open_weather_for_city(self: 'CityListPage', name: str) -> WeatherPage:
        self._get_city_el(name).click()
        return WeatherPage.instance(self.driver)

    def add_city(self: 'CityListPage', search_text: str, found_text: str) -> None:
        self.scroll_to(self.ADD_CITY).click()
        self.wait(self.SEARCH_CITY).send_keys(search_text)
        self.wait((By.XPATH, f'//*[contains(@name, "{found_text},")]')).click()

    def remove_city(self: 'CityListPage', name: str) -> None:
        el = self._get_city_el(name)
        self.swipe_in_el(el, relative_start_x=0.95, relative_end_x=0.55)
        self.wait(self.DELETE_CITY).click()



class CityListPageIOS(CityListPage):
    pass
