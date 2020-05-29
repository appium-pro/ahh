from selenium.webdriver.common.by import By
from pages import BasePage, TwHomePage


class TwLoginPage(BasePage):
    LOGIN_FIELD = (By.ID, "login_identifier")
    PW_FIELD = (By.ID, "login_password")
    LOGIN_BTN = (By.ID, "login_login")

    def login(self: 'TwLoginPage', username: str, pw: str) -> TwHomePage:
        self.wait(self.LOGIN_FIELD).send_keys(username)
        self.driver.find_element(*self.PW_FIELD).send_keys(pw)
        self.driver.find_element(*self.LOGIN_BTN).click()
        return TwHomePage(self.driver)
