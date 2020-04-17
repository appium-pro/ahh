from appium import webdriver
from pages.zoom.start_meeting_page import StartMeetingPage


class TestZoom(object):

    MEETING_ID = '75548979325'
    MEETING_PASS = '9mN2Rh'

    def test_join_meeting(self: 'TestZoom', driver: webdriver.Remote) -> None:
        start_meeting = StartMeetingPage(driver)
        start_meeting.join_meeting(self.MEETING_ID, self.MEETING_PASS)
