import os
from appium import webdriver
from conftest import MakeDriver
from lib.twilio import leave_voicemail
from pages import YMVoicemailsPage


JLIPPS_PHONE = os.getenv('JLIPPS_PHONE')


class TestYoumail(object):

    def test_voicemail_transcription(self: 'TestYoumail', make_driver: MakeDriver) -> None:
        msg = 'Hello everyone'
        driver: webdriver.Remote = make_driver('youmail')
        vms_page: YMVoicemailsPage = YMVoicemailsPage.instance(driver)
        assert not vms_page.has_messages()

        leave_voicemail(JLIPPS_PHONE, msg)

        vm_page = vms_page.open_voicemail(msg)
        vm_text = vm_page.get_voicemail_text()
        assert msg in vm_text
        vm_page.delete()
        assert not vms_page.has_messages()
