import time
from pages import BasePage, SearchPage


class ChooseLocPage(BasePage):
    LOCATION_FIELD = BasePage.text_locator('city or zip/postal code')
    CHOOSE_LOCATION = BasePage.text_locator('choose this location')

    def choose_location(self: 'ChooseLocPage', location: str, typed_location: str = None) -> SearchPage:
        if typed_location is None:
            typed_location = location
        self.wait(self.LOCATION_FIELD).send_keys(typed_location)
        self.wait(BasePage.text_locator(location)).click()
        choose = self.wait(self.CHOOSE_LOCATION)
        time.sleep(1)
        choose.click()
        return SearchPage.instance(self.driver)
