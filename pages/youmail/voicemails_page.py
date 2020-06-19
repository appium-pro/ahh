from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages import BasePage, YMVoicemailPage


class YMVoicemailsPage(BasePage):
    pass


class YMVoicemailsPageIOS(YMVoicemailsPage):

    NO_MESSAGES = (MobileBy.ACCESSIBILITY_ID, 'No messages yet.')

    def open_voicemail(self: 'YMVoicemailsPage', text: str) -> YMVoicemailPage:
        self.long_wait((By.XPATH, f'//XCUIElementTypeCell[contains(@value, "{text}")]')).click()
        return YMVoicemailPage.instance(self.driver)

    def has_messages(self: 'YMVoicemailsPage') -> bool:
        try:
            self.short_wait(self.NO_MESSAGES)
            return False
        except Exception:
            return True
