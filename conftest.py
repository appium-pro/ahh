import pytest
import os
from typing import Dict
from appium import webdriver


def get_driver(caps: Dict[str, str]) -> webdriver.Remote:
    driver = webdriver.Remote(
        command_executor='http://localhost:4723/wd/hub',
        desired_capabilities=caps
    )
    return driver


@pytest.fixture(scope='function')
def zoom_android_driver(zoom_android_caps: Dict[str, str]) -> webdriver.Remote:
    driver = get_driver(zoom_android_caps)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def zoom_ios_driver(zoom_ios_caps: Dict[str, str]) -> webdriver.Remote:
    driver = get_driver(zoom_ios_caps)
    yield driver
    driver.terminate_app('us.zoom.videomeetings')
    driver.quit()


@pytest.fixture()
def zoom_android_caps() -> Dict[str, str]:
    return {
        'platformName': 'Android',
        'deviceName': 'Android',
        'appPackage': 'us.zoom.videomeetings',
        'appActivity': 'com.zipow.videobox.LauncherActivity',
    }


@pytest.fixture()
def zoom_ios_caps() -> Dict[str, str]:
    return {
        'platformName': 'iOS',
        'platformVersion': '12.4',
        'deviceName': 'iPhone 5s',
        'bundleId': 'us.zoom.videomeetings',
        'udid': 'auto',
        'xcodeOrgId': os.environ.get('XCODE_ORG_ID'),
        'xcodeSigningId': 'iPhone Developer',
        'updatedWDABundleId': 'io.cloudgrey.wda',
        'automationName': 'XCUITest',
    }
