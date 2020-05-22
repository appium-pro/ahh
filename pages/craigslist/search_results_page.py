import os
import re
from selenium.webdriver.common.by import By
from pages import BasePage
from typing import List


FILTER_IMG = 'filter.png'
FILTER_IMG_PATH = os.path.join(os.path.dirname(__file__), FILTER_IMG)


class SearchResultsPage(BasePage):
    CATEGORY_DROPDOWN = BasePage.text_locator('category ▾')
    MAX_PRICE_FIELD = (By.XPATH, "//*[@text='price']/following-sibling::android.view.ViewGroup/android.widget.EditText[@text='max']")
    HAS_IMAGE = BasePage.text_locator('has image')
    APPLY = BasePage.text_locator('apply')

    def filter_max_price(self: 'SearchResultsPage', max_price: int) -> None:
        self.wait(self.CATEGORY_DROPDOWN)
        self.driver.find_element_by_image(FILTER_IMG_PATH).click()
        self.wait(self.MAX_PRICE_FIELD).send_keys(max_price)
        self.wait(self.APPLY).click()

    def get_prices(self: 'SearchResultsPage') -> List[int]:
        self.wait(self.CATEGORY_DROPDOWN)
        non_number = re.compile("[^0-9]")
        return list(map(
            lambda el: int(re.sub(non_number, "", el.text)),
            self.driver.find_elements(By.XPATH, '//*[starts-with(@text, "$")]')
        ))
