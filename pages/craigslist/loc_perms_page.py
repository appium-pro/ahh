from selenium.webdriver.common.by import By
from pages import BasePage, ChooseLocPage


class LocPermsPage(BasePage):
    SHARE_LOCATION = BasePage.text_locator('share location')
    ALLOW_LOCATION = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')

    def share_location(self: 'LocPermsPage') -> ChooseLocPage:
        self.wait(self.SHARE_LOCATION).click()
        self.wait(self.ALLOW_LOCATION).click()
        return ChooseLocPage.instance(self.driver)
