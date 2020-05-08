from appium import webdriver
from pages import StartMeetingPage, NotesPage


NOTES_BUNDLE_ID = 'com.apple.mobilenotes'
ZOOM_BUNDLE_ID = 'us.zoom.videomeetings'
ANDROID_USER_NAME = 'JLipps S7'


class TestZoom(object):

    MEETING_ID = '75548979325'
    MEETING_PASS = '9mN2Rh'

    def test_join_meeting(self: 'TestZoom', zoom_android_driver: webdriver.Remote) -> None:
        start_meeting = StartMeetingPage.instance(zoom_android_driver)
        start_meeting.join_meeting(self.MEETING_ID, self.MEETING_PASS)

    def test_create_and_join_meeting(self: 'TestZoom', zoom_ios_driver: webdriver.Remote,
            zoom_android_driver: webdriver.Remote) -> None:
        # 1. DONE ios - start a meeting
        # 2. DONE ios - scrape the meeting credentials
        # 3. android - use credentials to join a meeting
        start_ios = StartMeetingPage.instance(zoom_ios_driver)
        meeting_ios = start_ios.start_meeting()
        meeting_ios.join_audio()
        meeting_ios.copy_invite_url()
        zoom_ios_driver.terminate_app(NOTES_BUNDLE_ID)
        zoom_ios_driver.activate_app(NOTES_BUNDLE_ID)
        notes_ios = NotesPage.instance(zoom_ios_driver)
        invite_url = notes_ios.get_clipboard_text()
        # TODO update meeting creds logic to use personal meeting with no password
        (meeting_id, meeting_pw) = meeting_ios.get_meeting_creds(invite_url)
        print(meeting_id)
        print(meeting_pw)
        notes_ios.back_to_call()

        # 3. android - use credentials to join a meeting
        start_android = StartMeetingPage.instance(zoom_android_driver)
        start_android.join_meeting(meeting_id, meeting_pw)

        # 4a. ios - admit the android user
        meeting_ios.admit_participant(ANDROID_USER_NAME)

        # 4b. ios - confirm that android joined
        assert meeting_ios.participant_is_present(ANDROID_USER_NAME)

        # 5. android - leave the meeting
        start_android.leave_meeting()

        # 6. ios - confirm that android left
        assert not meeting_ios.participant_is_present(ANDROID_USER_NAME)

        # 7. ios - end the meeting
        meeting_ios.end_meeting()
