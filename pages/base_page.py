from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from typing import Tuple


class BasePage(object):

    def __init__(self: 'BasePage', driver: webdriver.Remote) -> 'BasePage':
        self.driver = driver
        self._wait = WebDriverWait(driver, 10)

    def wait(self: 'BasePage', locator: Tuple[By, str]) -> WebElement:
        return self._wait.until(EC.presence_of_element_located(locator))
