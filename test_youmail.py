import os
from appium import webdriver
from conftest import MakeDriver
from lib.twilio import leave_voicemail


JLIPPS_PHONE = os.getenv('JLIPPS_PHONE')


class TestYoumail(object):

    def test_voicemail_transcription(self: 'TestYoumail', make_driver: MakeDriver) -> None:
        msg = 'Hello from the live stream'
        leave_voicemail(JLIPPS_PHONE, msg)
        # driver: webdriver.Remote = make_driver('youmail')
        # print(driver.page_source)
