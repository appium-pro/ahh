from selenium.webdriver.common.by import By
from pages import BasePage, LocPermsPage


class GetStartedPage(BasePage):
    GET_STARTED_BUTTON = BasePage.text_locator('get started')

    def get_started(self: 'GetStartedPage') -> LocPermsPage:
        self.wait(self.GET_STARTED_BUTTON).click()
        return LocPermsPage.instance(self.driver)
