from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages import BasePage, TwSearchPage


class TwHomePage(BasePage):
    BTN1 = (By.ID, 'android:id/button1')
    BTN2 = (By.ID, 'android:id/button2')
    MENU = (MobileBy.ACCESSIBILITY_ID, 'Show navigation drawer')
    SETTINGS_MENU = BasePage.text_locator('Settings and privacy')
    ACCOUNT_MENU = BasePage.text_locator('Account')
    LOGIN_AND_SECURITY = BasePage.text_locator('Login and security')
    LOG_OUT = BasePage.text_locator('Log out')
    SEARCH_ICON = (MobileBy.ACCESSIBILITY_ID, 'Explore')  # TODO

    def allow_data_collection(self: 'TwHomePage') -> None:
        self.wait(self.BTN1).click()

    def skip_location_settings(self: 'TwHomePage') -> None:
        self.wait(self.BTN2).click()

    def open_menu(self: 'TwHomePage') -> None:
        self.wait(self.MENU).click()

    def logout(self: 'TwHomePage') -> None:
        self.open_menu()
        self.wait(self.SETTINGS_MENU).click()
        self.wait(self.ACCOUNT_MENU).click()
        self.wait(self.LOGIN_AND_SECURITY)
        self.scroll_to(self.LOG_OUT).click()
        self.wait(self.BTN1).click()

    def nav_to_search(self: 'TwSearchPage') -> TwSearchPage:
        self.wait(self.SEARCH_ICON).click()
        return TwSearchPage.instance(self.driver)
