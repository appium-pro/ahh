import pytest
from typing import Dict
from appium import webdriver


@pytest.fixture(scope='function')
def driver(zoom_caps: Dict[str, str]) -> webdriver.Remote:
    driver = webdriver.Remote(
        command_executor='http://localhost:4723/wd/hub',
        desired_capabilities=zoom_caps
    )
    yield driver
    driver.quit()


@pytest.fixture()
def zoom_caps() -> Dict[str, str]:
    return {
        'platformName': 'Android',
        'deviceName': 'Android',
        'appPackage': 'us.zoom.videomeetings',
        'appActivity': 'com.zipow.videobox.LauncherActivity',
    }
