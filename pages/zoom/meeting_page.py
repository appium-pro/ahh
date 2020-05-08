from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from ..base_page import BasePage
from typing import Tuple, List
import re


class MeetingPage(BasePage):
    CALL_USING_INTERNET = (By.ID, '')
    PARTICIPANTS_TAB = (By.ID, '')
    INVITE = (By.ID, '')
    COPY_URL = (By.ID, '')
    END_MEETING = (By.ID, '')
    ACTUALLY_END_MEETING = (By.ID, '')
    PARTICIPANTS = (By.XPATH, '')
    LEAVE_MEETING = (By.ID, 'btnLeave')
    ACTUALLY_LEAVE_MEETING = (By.ID, 'btnLeaveMeeting')

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

    def copy_invite_url(self: 'MeetingPage') -> None:
        self.ensure_ui_present()
        self.wait(self.PARTICIPANTS_TAB).click()
        self.wait(self.INVITE).click()
        self.wait(self.COPY_URL).click()
        self.driver.back()

    def leave_meeting(self: 'MeetingPage') -> None:
        self.wait(self.LEAVE_MEETING).click()
        self.wait(self.ACTUALLY_LEAVE_MEETING).click()

    def end_meeting(self: 'MeetingPage') -> str:
        self.ensure_ui_present()
        self.wait(self.END_MEETING).click()
        self.wait(self.ACTUALLY_END_MEETING).click()
        # TODO wait for the home screen UI to show up

    def get_meeting_creds(self: 'MeetingPage', url: str) -> Tuple[str, str]:
        match = re.match('^https.+?([0-9]+)(\?pwd=(.+))?$', url)
        groups = match.groups()
        return (groups[0], groups[2])

    def admit_participant(self: 'MeetingPage', name: str) -> None:
        self.ensure_ui_present()
        self.wait(self.PARTICIPANTS_TAB).click()
        self.tap_el(self.wait((By.XPATH, f"//XCUIElementTypeStaticText[contains(@name, '{name}')]/following-sibling::XCUIElementTypeButton[@name='Admit']")))
        self.back()

    def participant_is_present(self: 'MeetingPage', name: str) -> bool:
        self.ensure_ui_present()
        self.wait(self.PARTICIPANTS_TAB).click()
        self.wait(self.INVITE)
        try:
            self.wait((By.XPATH, f'//*[contains(@name, {name})]'))
            return True
        except Exception:
            return False
        finally:
            self.driver.back()


class MeetingPageIOS(MeetingPage):
    CALL_USING_INTERNET = (By.XPATH, '//*[contains(@name, "Call")]')
    PARTICIPANTS_TAB = (MobileBy.ACCESSIBILITY_ID, 'Participants')
    INVITE = (MobileBy.ACCESSIBILITY_ID, 'Invite')
    COPY_URL = (MobileBy.ACCESSIBILITY_ID, 'Copy URL')
    END_MEETING = (MobileBy.ACCESSIBILITY_ID, 'End')
    ACTUALLY_END_MEETING = (MobileBy.ACCESSIBILITY_ID, 'End Meeting')
    PARTICIPANTS = (By.XPATH, '//*[contains(@name, "udio") and contains(@name, "ideo")]')
