from appium import webdriver
from pages import StartMeetingPage, NotesPage


NOTES_BUNDLE_ID = 'com.apple.mobilenotes'
ZOOM_BUNDLE_ID = 'us.zoom.videomeetings'


class TestZoom(object):

    MEETING_ID = '75548979325'
    MEETING_PASS = '9mN2Rh'

    def test_join_meeting(self: 'TestZoom', zoom_android_driver: webdriver.Remote) -> None:
        start_meeting = StartMeetingPage.instance(zoom_android_driver)
        start_meeting.join_meeting(self.MEETING_ID, self.MEETING_PASS)

    def test_create_and_join_meeting(self: 'TestZoom', zoom_ios_driver: webdriver.Remote) -> None:
        # 1. DONE ios - start a meeting
        # 2. DONE ios - scrape the meeting credentials
        # 3. android - use credentials to join a meeting
        # 4. ios - confirm that android joined
        # 5. ios - end meeting
        # 6. android - verify meeting ended
        start = StartMeetingPage.instance(zoom_ios_driver)
        meeting = start.start_meeting()
        meeting.join_audio()
        meeting.copy_invite_url()
        zoom_ios_driver.activate_app(NOTES_BUNDLE_ID)
        notes = NotesPage.instance(zoom_ios_driver)
        invite_url = notes.get_clipboard_text()
        print(invite_url)
        zoom_ios_driver.activate_app(ZOOM_BUNDLE_ID)
        meeting.end_meeting()
        raise Exception('ok')
