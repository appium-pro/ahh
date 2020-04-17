from appium import webdriver
import time


class TestZoom(object):

    def test_join_meeting(self: 'TestZoom', driver: webdriver.Remote) -> None:
        driver.find_element_by_id('btnJoinConf').click()
