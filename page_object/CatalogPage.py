from page_object.Base import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@class= 'button-group']/button[1]")
    SORT_INPUT = (By.CSS_SELECTOR, "#input-sort")
    LIMIT_INPUT = (By.CSS_SELECTOR, "#input-limit")
    PRICE = (By.CSS_SELECTOR, "p.price")

    def check_existing_of_list_view_element(self):
        return self._existing_of_elements(*self.LIST_VIEW)

    def check_existing_of_add_to_cart_button(self):
        return self._existing_of_elements(*self.ADD_TO_CART_BUTTON)

    def check_existing_of_sort_input(self):
        return self._existing_of_elements(*self.SORT_INPUT)

    def check_existing_of_limit_input(self):
        return self._existing_of_elements(*self.LIMIT_INPUT)

    def check_existing_of_price(self):
        return self._existing_of_elements(*self.PRICE)
