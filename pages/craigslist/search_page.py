from pages import BasePage, SearchResultsPage


class SearchPage(BasePage):

    def browse_category(self: 'SearchPage', category: str, subcategory: str) -> SearchResultsPage:
        self.wait(BasePage.text_locator(category)).click()
        self.wait(BasePage.text_locator(subcategory)).click()
        return SearchResultsPage.instance(self.driver)
