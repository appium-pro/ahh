from selenium.webdriver.common.by import By
from pages import BasePage, TwLoginPage


class TwSplashPage(BasePage):
    LOGIN_BTN = (By.ID, "detail_text")

    def nav_to_login(self: 'TwSplashPage') -> TwLoginPage:
        el = self.wait(self.LOGIN_BTN)
        self.tap_el_at(el, 0.9, 0.5)
        return TwLoginPage(self.driver)

    def verify(self: 'TwSplashPage') -> None:
        self.wait(self.LOGIN_BTN)
