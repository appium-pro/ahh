from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from ..base_page import BasePage
from .meeting_page import MeetingPage, MeetingPageIOS


class StartMeetingPage(BasePage):
    JOIN_MEETING_BUTTON = (By.ID, 'btnJoinConf')
    MEETING_ID_FIELD = (By.ID, 'edtConfNumber')
    ACTUALLY_JOIN_MEETING_BUTTON = (By.ID, 'btnJoin')
    PASSWORD_FIELD = (By.ID, 'edtPassword')
    PASSWORD_OK_BUTTON = (By.ID, 'button1')
    LEAVE_BTN = (By.ID, 'btnLeave')
    START_MEETING_BUTTON = (By.ID, '')
    ACTUALLY_START_MEETING_BUTTON = (By.ID, '')
    ADD_CONTACTS = (By.ID, '')

    def __init__(self: 'StartMeetingPage', driver: webdriver.Remote) -> 'StartMeetingPage':
        super().__init__(driver)

    def start_meeting(self: 'StartMeetingPage') -> MeetingPage:
        self.wait(self.ADD_CONTACTS)
        self.tap_el(self.wait(self.START_MEETING_BUTTON))
        self.wait(self.ACTUALLY_START_MEETING_BUTTON).click()
        return MeetingPage(self.driver)

    def join_meeting(self: 'StartMeetingPage', meeting_id: str, meeting_pass: str) -> None:
        self.wait(self.JOIN_MEETING_BUTTON).click()
        self.wait(self.MEETING_ID_FIELD).send_keys(meeting_id)
        self.driver.find_element(*self.ACTUALLY_JOIN_MEETING_BUTTON).click()
        self.wait(self.PASSWORD_FIELD).send_keys(meeting_pass)
        self.driver.find_element(*self.PASSWORD_OK_BUTTON).click()
        self.wait(self.LEAVE_BTN)


class StartMeetingPageIOS(StartMeetingPage):
    START_MEETING_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'New Meeting')
    ACTUALLY_START_MEETING_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Start a Meeting"]')
    ADD_CONTACTS = (MobileBy.ACCESSIBILITY_ID, 'Add Contacts')

    def start_meeting(self: 'StartMeetingPage') -> MeetingPageIOS:
        super().start_meeting()
        return MeetingPageIOS(self.driver)
