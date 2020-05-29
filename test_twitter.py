import os
from appium import webdriver
from conftest import MakeDriver
from pages import TwSplashPage


USERNAME = os.getenv('TW_USERNAME')
PASSWORD = os.getenv('TW_PASSWORD')


class TestTwitter(object):

    def test_login_and_logout(self: 'TestTwitter', make_driver: MakeDriver) -> None:
        d: webdriver.Remote = make_driver("twitter")
        splash_page = TwSplashPage(d)
        login_page = splash_page.nav_to_login()
        home_page = login_page.login(USERNAME, PASSWORD)
        home_page.allow_data_collection()
        home_page.skip_location_settings()
        home_page.logout()
        splash_page.verify()
