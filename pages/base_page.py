from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from appium import webdriver
from typing import Tuple


class BasePage(object):

    def __init__(self: 'BasePage', driver: webdriver.Remote) -> 'BasePage':
        self.driver = driver
        self._wait = WebDriverWait(driver, 10)
        self._short_wait = WebDriverWait(driver, 3)

    def wait(self: 'BasePage', locator: Tuple[By, str], waiter: WebDriverWait = None) -> WebElement:
        if waiter is None:
            waiter = self._wait
        return waiter.until(EC.presence_of_element_located(locator))

    def short_wait(self: 'BasePage', locator: Tuple[By, str]) -> WebElement:
        return self.wait(locator, waiter=self._short_wait)

    def tap_at(self: 'BasePage', x: int, y: int) -> None:
        actions = ActionBuilder(self.driver)
        p = actions.add_pointer_input("touch", "finger")
        p_actions = PointerActions(p)
        p.create_pointer_move(duration=0, x=x, y=y, origin='viewport')
        p_actions.pointer_down()
        p_actions.pause(0.2)
        p_actions.pointer_up()
        actions.perform()

    def tap_el(self: 'BasePage', el: WebElement) -> None:
        rect = el.rect
        x = rect['x'] + (rect['width'] / 2)
        y = rect['y'] + (rect['height'] / 2)
        self.tap_at(x, y)
