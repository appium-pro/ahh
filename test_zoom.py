from appium import webdriver
from pages.zoom.start_meeting_page import StartMeetingPage, StartMeetingPageIOS


class TestZoom(object):

    MEETING_ID = '75548979325'
    MEETING_PASS = '9mN2Rh'

    def test_join_meeting(self: 'TestZoom', zoom_android_driver: webdriver.Remote) -> None:
        start_meeting = StartMeetingPage(zoom_android_driver)
        start_meeting.join_meeting(self.MEETING_ID, self.MEETING_PASS)

    def test_create_and_join_meeting(self: 'TestZoom', zoom_ios_driver: webdriver.Remote) -> None:
        # 1. DONE ios - start a meeting
        # 2. DONE ios - scrape the meeting credentials
        # 3. android - use credentials to join a meeting
        # 4. ios - confirm that android joined
        # 5. ios - end meeting
        # 6. android - verify meeting ended
        start = StartMeetingPageIOS(zoom_ios_driver)
        meeting = start.start_meeting()
        invite_url = meeting.get_invite_url()
        print(invite_url)
        raise Exception('ok')
