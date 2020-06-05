from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages import BasePage, TwProfilePage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pages import TwHomePage


class TwSearchPage(BasePage):
    ENABLE_SEARCH_BTN = (By.ID, 'query_view')
    SEARCH_BOX = (MobileBy.ACCESSIBILITY_ID, 'Search')
    HOME_TAB = (MobileBy.ACCESSIBILITY_ID, 'Home Tab')

    def search_for_user(self: 'TwSearchPage', username: str) -> TwProfilePage:
        self.wait(self.ENABLE_SEARCH_BTN).click()
        self.wait(self.SEARCH_BOX).send_keys(username)
        self.wait(BasePage.text_locator(f'@{username}')).click()
        return TwProfilePage.instance(self.driver)

    def nav_to_home(self: 'TwSearchPage') -> 'TwHomePage':
        from pages import TwHomePage
        self.wait(self.HOME_TAB).click()
        return TwHomePage.instance(self.driver)
