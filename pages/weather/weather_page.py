import re
from pages import BasePage
from typing import TYPE_CHECKING, List, Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from appium.webdriver.common.mobileby import MobileBy
if TYPE_CHECKING:
    from pages import CityListPage

NON_NUMBER = re.compile("[^0-9]")


def get_nums(text: str) -> int:
    return int(re.sub(NON_NUMBER, "", text))


class WeatherPage(BasePage):

    HOURLY_FORECASTS = (By.XPATH, '//XCUIElementTypeCollectionView[@name="Hourly Forecasts"]/XCUIElementTypeCell')
    DAILY_FORECASTS = (By.XPATH, '//XCUIElementTypeScrollView[@name="Daily Forecasts"]/XCUIElementTypeOther')
    EDIT_CITIES = (MobileBy.ACCESSIBILITY_ID, 'Edit Cities')

    def get_hourly_weather(self: 'WeatherPage') -> List[Dict]:
        els = self.driver.find_elements(*self.HOURLY_FORECASTS)

        def parse_data_from_cell(cell: WebElement) -> Dict:
            data = cell.get_attribute('name').split(',')
            print(data)
            if len(data) != 3:
                return None
            return {
                'time': data[0],
                'weather': data[1].strip(),
                'temp': get_nums(data[2]),
            }

        return list(filter(lambda val: val is not None, map(parse_data_from_cell, els)))


    def get_daily_weather(self: 'WeatherPage') -> None:
        els = self.driver.find_elements(*self.DAILY_FORECASTS)

        def parse_data_from_cell(cell: WebElement) -> Dict:
            name = cell.get_attribute('name')
            if type(name) != str:
                return None
            data = name.split(',')
            print(data)
            if len(data) != 4:
                return None
            return {
                'day': data[0],
                'weather': data[1].strip(),
                'high_temp': get_nums(data[2]),
                'low_temp': get_nums(data[3]),
            }

        return list(filter(lambda val: val is not None, map(parse_data_from_cell, els)))

    def get_sunrise(self: 'WeatherPage') -> None:
        pass

    def open_city_list(self: 'WeatherPage') -> 'CityListPage':
        from pages import CityListPage
        self.wait(self.EDIT_CITIES).click()
        return CityListPage.instance(self.driver)


class WeatherPageIOS(WeatherPage):
    pass
