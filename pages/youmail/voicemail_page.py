from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages import BasePage


class YMVoicemailPage(BasePage):
    pass


class YMVoicemailPageIOS(YMVoicemailPage):
    DELETE_MESSAGE = (MobileBy.ACCESSIBILITY_ID, 'delete message')
    VM_TEXT = (By.XPATH, '//XCUIElementTypeButton[contains(@label, "Accurate")]/preceding-sibling::XCUIElementTypeStaticText')

    def delete(self: 'YMVoicemailPage') -> None:
        self.wait(self.DELETE_MESSAGE).click()

    def get_voicemail_text(self: 'YMVoicemailPage') -> str:
        return self.wait(self.VM_TEXT).text
