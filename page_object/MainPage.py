from page_object.Base import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH_INPUT = (By.XPATH, "//div[@id='search']")
    CURRENCY = (By.CSS_SELECTOR, "div.pull_left")
    ABOUT_US_BUTTON = (By.LINK_TEXT, "About us")
    WISH_LIST = (By.CSS_SELECTOR, "#wishlist-total")

    def check_existing_of_logo(self):
        return self._existing_of_elements(*self.LOGO)

    def check_existing_of_search(self):
        return self._existing_of_elements(*self.SEARCH_INPUT)

    def check_existing_of_currency(self):
        return self._existing_of_elements(*self.CURRENCY)

    def check_existing_about_us(self):
        return self._existing_of_elements(*self.ABOUT_US_BUTTON)

    def check_existing_of_wish_list(self):
        return self._existing_of_elements(*self.WISH_LIST)
