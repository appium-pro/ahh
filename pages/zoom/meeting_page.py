from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from ..base_page import BasePage


class MeetingPage(BasePage):
    CALL_USING_INTERNET = (By.ID, '')
    PARTICIPANTS_TAB = (By.ID, '')
    INVITE = (By.ID, '')
    COPY_URL = (By.ID, '')
    END_MEETING = (By.ID, '')

    def __init__(self: 'MeetingPage', driver: webdriver.Remote) -> 'MeetingPage':
        super().__init__(driver)

    def ensure_ui_present(self: 'MeetingPage') -> None:
        try:
            self.short_wait(self.END_MEETING)
            return
        except Exception:
            size = self.driver.get_window_size()
            x = size['width'] / 2
            y = size['height'] / 2
            self.tap_at(x=x, y=y)

    def join_audio(self: 'MeetingPage') -> None:
        self.wait(self.CALL_USING_INTERNET).click()

    def get_invite_url(self: 'MeetingPage') -> str:
        self.ensure_ui_present()
        self.wait(self.PARTICIPANTS_TAB).click()
        self.wait(self.INVITE).click()
        url = self.driver.get_clipboard_text()
        self.driver.back()
        return url

    def end_meeting(self: 'MeetingPage') -> str:
        self.ensure_ui_present()
        self.wait(self.END_MEETING).click()


class MeetingPageIOS(MeetingPage):
    CALL_USING_INTERNET = (By.XPATH, '//*[contains(@name, "Call")]')
    PARTICIPANTS_TAB = (MobileBy.ACCESSIBILITY_ID, 'Participants')
    INVITE = (MobileBy.ACCESSIBILITY_ID, 'Invite')
    COPY_URL = (MobileBy.ACCESSIBILITY_ID, 'Open URL')
    END_MEETING = (MobileBy.ACCESSIBILITY_ID, 'End')
