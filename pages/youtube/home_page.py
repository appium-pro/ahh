from pages import BasePage, YTSearchResultsPage
from appium.webdriver.common.mobileby import MobileBy


class YTHomePage(BasePage):

    SEARCH_ICON = (MobileBy.ACCESSIBILITY_ID, 'Search')
    SEARCH_FIELD = (MobileBy.ID, 'search_edit_text')

    def search(self: 'YTHomePage', term: str) -> YTSearchResultsPage:
        self.wait(self.SEARCH_ICON).click()
        self.wait(self.SEARCH_FIELD).send_keys(f'{term}\\n')
        return YTSearchResultsPage.instance(self.driver)
