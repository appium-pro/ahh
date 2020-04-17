from selenium.webdriver.common.by import By
from appium import webdriver
from ..base_page import BasePage


class StartMeetingPage(BasePage):
    JOIN_MEETING_BUTTON = (By.ID, 'btnJoinConf')
    MEETING_ID_FIELD = (By.ID, 'edtConfNumber')
    ACTUALLY_JOIN_MEETING_BUTTON = (By.ID, 'btnJoin')
    PASSWORD_FIELD = (By.ID, 'edtPassword')
    PASSWORD_OK_BUTTON = (By.ID, 'button1')
    LEAVE_BTN = (By.ID, 'btnLeave')

    def __init__(self: 'StartMeetingPage', driver: webdriver.Remote) -> 'StartMeetingPage':
        super().__init__(driver)

    def join_meeting(self: 'StartMeetingPage', meeting_id: str, meeting_pass: str) -> None:
        self.wait(self.JOIN_MEETING_BUTTON).click()
        self.wait(self.MEETING_ID_FIELD).send_keys(meeting_id)
        self.driver.find_element(*self.ACTUALLY_JOIN_MEETING_BUTTON).click()
        self.wait(self.PASSWORD_FIELD).send_keys(meeting_pass)
        self.driver.find_element(*self.PASSWORD_OK_BUTTON).click()
        self.wait(self.LEAVE_BTN)
