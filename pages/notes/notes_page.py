from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages import BasePage


class NotesPage(BasePage):
    NEW_NOTE = (By.ID, '')
    NOTE = (By.ID, '')
    PASTE = (By.ID, '')
    LINK = (By.ID, '')

    def get_clipboard_text(self: 'NotesPage') -> str:
        self.wait(self.NEW_NOTE).click()
        self.tap_el(self.wait(self.NOTE))
        self.wait(self.PASTE).click()
        return self.wait(self.LINK).text

    def back_to_call(self: 'NotesPage') -> None:
        self.tap_at(100, 5)


class NotesPageIOS(NotesPage):
    NEW_NOTE = (MobileBy.ACCESSIBILITY_ID, 'New note')
    NOTE = (MobileBy.ACCESSIBILITY_ID, 'note')
    PASTE = (MobileBy.ACCESSIBILITY_ID, 'Paste')
    LINK = (By.XPATH, "//XCUIElementTypeTextView[@name='note']/XCUIElementTypeLink")
