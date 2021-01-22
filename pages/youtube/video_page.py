from pages import BasePage, Locator
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException


LIKE_XPATH = '//*[contains(@content-desc, "like this video")]'


class YTVideoPage(BasePage):

    LIKE_BUTTON = (MobileBy.XPATH, LIKE_XPATH)
    LIKE_COUNT = (MobileBy.XPATH, f'{LIKE_XPATH}/following-sibling::*[contains(@resource-id, "button_text")]')
    EXPAND = (MobileBy.ACCESSIBILITY_ID, 'Expand Mini Player')
    PAUSE = (MobileBy.ACCESSIBILITY_ID, 'Pause video')
    PLAY = (MobileBy.ACCESSIBILITY_ID, 'Play video')
    MINIMIZE = (MobileBy.ACCESSIBILITY_ID, 'Minimize')
    CLOSE = (MobileBy.ACCESSIBILITY_ID, 'Close miniplayer')
    HOME = (MobileBy.ACCESSIBILITY_ID, 'Home')

    def like(self: 'YTVideoPage') -> None:
        self.wait(self.LIKE_BUTTON).click()

    def get_num_likes(self: 'YTVideoPage') -> int:
        return int(self.long_wait(self.LIKE_COUNT).text)

    def _mini_control(self: 'YTVideoPage', control: Locator) -> None:
        try:
            self.short_wait(control).click()
            return
        except TimeoutException:
            pass
        self.wait(self.EXPAND).click()
        self.short_wait(control).click()

    def pause(self: 'YTVideoPage') -> None:
        self._mini_control(self.PAUSE)

    def play(self: 'YTVideoPage') -> None:
        self._mini_control(self.PLAY)

    def minimize(self: 'YTVideoPage') -> None:
        self._mini_control(self.MINIMIZE)

    def close(self: 'YTVideoPage') -> None:
        self.wait(self.CLOSE).click()

    def navigate_to_home(self: 'YTVideoPage') -> None:
        self.wait(self.HOME).click()
