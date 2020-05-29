import importlib
import enum
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from appium import webdriver
from typing import Tuple, TypeVar


T = TypeVar('T')
Locator = Tuple[By, str]


class ScrollDirection(enum.Enum):
    down = enum.auto()
    left = enum.auto()
    right = enum.auto()
    up = enum.auto()


def class_for_name(module_name: str, class_name: str) -> type:
    """ This is a helper method to get a class reference dynamically """
    m = importlib.import_module(module_name)
    return getattr(m, class_name)


class nonzero_size(object):
    def __init__(self, el: WebElement) -> 'nonzero_size':
        self.el = el

    def __call__(self, driver: webdriver.Remote):
        rect = self.el.rect
        return rect['width'] != 0 and rect['height'] != 0


class has_url_text(object):
    def __init__(self: 'has_url_text', el: WebElement) -> 'has_url_text':
        self.el = el

    def __call__(self: 'has_url_text', driver: webdriver.Remote):
        text: str = self.el.get_attribute('value')
        return text.startswith('http')


class BasePage(object):

    def __init__(self: 'BasePage', driver: webdriver.Remote) -> 'BasePage':
        self.driver = driver
        self._wait = WebDriverWait(driver, 10)
        self._short_wait = WebDriverWait(driver, 3)
        self._long_wait = WebDriverWait(driver, 30)

    def wait(self: 'BasePage', locator: Locator, waiter: WebDriverWait = None) -> WebElement:
        if waiter is None:
            waiter = self._wait
        return waiter.until(EC.presence_of_element_located(locator))

    def short_wait(self: 'BasePage', locator: Locator) -> WebElement:
        return self.wait(locator, waiter=self._short_wait)

    def long_wait(self: 'BasePage', locator: Locator) -> WebElement:
        return self.wait(locator, waiter=self._long_wait)

    def wait_for_nonzero_size(self: 'BasePage', locator: Locator) -> WebElement:
        el = self.wait(locator)
        self._wait.until(nonzero_size(el))
        return el

    def wait_for_url(self: 'BasePage', locator: Locator) -> str:
        el = self.wait(locator)
        self._wait.until(has_url_text(el))
        return el.get_attribute('value')

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

    def tap_el_at(self: 'BasePage', el: WebElement, x_pct: float, y_pct: float) -> None:
        rect = el.rect
        x = rect['x'] + (rect['width'] * x_pct)
        y = rect['y'] + (rect['height'] * y_pct)
        self.tap_at(x, y)

    def swipe_by_pixels(self, start_x: int, start_y: int, end_x: int, end_y: int,
                        duration_ms: int = 1500) -> None:
        actions = ActionBuilder(self.driver)
        p = actions.add_pointer_input("touch", "finger1")
        p_actions = PointerActions(p)
        p.create_pointer_move(duration=0, x=start_x, y=start_y, origin='viewport')
        p_actions.pointer_down()
        p.create_pointer_move(duration=duration_ms, x=end_x, y=end_y, origin='viewport')
        p_actions.pointer_up()
        actions.perform()

    def swipe(self, relative_start_x: float, relative_start_y: float, relative_end_x: float,
              relative_end_y: float, duration_ms: int = 200) -> None:
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        start_x = int(width * relative_start_x)
        start_y = int(height * relative_start_y)
        end_x = int(width * relative_end_x)
        end_y = int(height * relative_end_y)
        self.swipe_by_pixels(start_x, start_y, end_x, end_y, duration_ms)

    def scroll(self, direction: ScrollDirection, amount: float = 0.5,
               duration_ms: int = 200) -> None:
        relative_start_x = 0.5
        relative_start_y = 0.5
        relative_end_x = 0.5
        relative_end_y = 0.5
        if direction == ScrollDirection.down:
            relative_start_y += amount / 2
            relative_end_y -= amount / 2
        elif direction == ScrollDirection.up:
            relative_start_y -= amount / 2
            relative_end_y += amount / 2
        elif direction == ScrollDirection.left:
            relative_start_x -= amount / 2
            relative_end_x += amount / 2
        elif direction == ScrollDirection.right:
            relative_start_x += amount / 2
            relative_end_x -= amount / 2
        else:
            raise ValueError("Scroll direction is not valid")
        self.swipe(relative_start_x, relative_start_y, relative_end_x, relative_end_y, duration_ms)

    def scroll_to(self, locator: Locator, max_scrolls: int = 10,
                  direction: ScrollDirection = ScrollDirection.down) -> WebElement:
        scrolls = 0
        while scrolls < max_scrolls:
            try:
                return self.driver.find_element(*locator)
            except NoSuchElementException:
                self.scroll(direction)
            scrolls += 1
        raise NoSuchElementException(f'Could not find element after {max_scrolls} scrolls')

    @classmethod
    def instance(cls: T, driver: webdriver.Remote) -> T:
        plat = driver.capabilities['platformName'].lower()
        klass = cls.__name__
        if plat != 'android':
            klass = f'{klass}IOS'
        return class_for_name('pages', klass)(driver)

    @staticmethod
    def text_locator(text: str) -> Locator:
        return (By.XPATH, f'//*[@text="{text}"]')
