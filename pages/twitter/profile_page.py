from selenium.webdriver.common.by import By
from pages import BasePage


class TwProfilePage(BasePage):
    BTN1 = (By.ID, 'android:id/button1')
    FOLLOW_BTN = (By.ID, 'button_bar_follow')
    UNFOLLOW_BTN = (By.ID, 'button_bar_following')

    def follow(self: 'TwProfilePage') -> None:
        self.wait(self.FOLLOW_BTN).click()
        self.wait(self.UNFOLLOW_BTN)

    def unfollow(self: 'TwProfilePage') -> None:
        self.wait(self.UNFOLLOW_BTN).click()
        self.wait(self.BTN1).click()
        self.wait(self.FOLLOW_BTN)
