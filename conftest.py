import pytest
import os
from appium import webdriver
from typing import Callable


MakeDriver = Callable[[str], webdriver.Remote]


ZOOM_ANDROID_CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'appPackage': 'us.zoom.videomeetings',
    'appActivity': 'com.zipow.videobox.LauncherActivity',
    'automationName': 'UiAutomator2',
    'newCommandTimeout': 300,
}


ZOOM_IOS_CAPS = {
    'platformName': 'iOS',
    'platformVersion': '12.4',
    'deviceName': 'iPhone 5s',
    'bundleId': 'us.zoom.videomeetings',
    'udid': 'auto',
    'xcodeOrgId': os.environ.get('XCODE_ORG_ID'),
    'xcodeSigningId': 'iPhone Developer',
    'updatedWDABundleId': 'io.cloudgrey.wda',
    'automationName': 'XCUITest',
    'newCommandTimeout': 300,
}


CRAIGSLIST_ANDROID_CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'app': '/Users/jlipps/Code/testapps/craigslist.apk',
    'appWaitActivity': 'org.craigslist.CraigslistMobile.MainActivity',
    'automationName': 'UiAutomator2',
    'newCommandTimeout': 300,
}


TWITTER_ANDROID_CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'app': '/Users/jlipps/Code/testapps/twitter.apk',
    'appWaitActivity': 'com.twitter.app.main.MainActivity',
    'automationName': 'UiAutomator2',
    'newCommandTimeout': 300,
}


@pytest.fixture
def make_driver() -> webdriver.Remote:
    driver = None

    def _make_driver(app: str) -> webdriver.Remote:
        nonlocal driver
        if app == "zoom_android":
            caps = ZOOM_ANDROID_CAPS
        elif app == "zoom_ios":
            caps = ZOOM_IOS_CAPS
        elif app == "craigslist":
            caps = CRAIGSLIST_ANDROID_CAPS
        elif app == "twitter":
            caps = TWITTER_ANDROID_CAPS
        driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities=caps
        )
        return driver

    yield _make_driver
    driver.quit()
