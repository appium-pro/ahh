from pages import BasePage, YTVideoPage
from appium.webdriver.common.mobileby import MobileBy


class YTSearchResultsPage(BasePage):

    def play_video(self: 'YTSearchResultsPage', title: str) -> YTVideoPage:
        self.scroll_to((MobileBy.XPATH, f'//android.view.ViewGroup[contains(@content-desc, "{title}")]')).click()
        return YTVideoPage.instance(self.driver)
