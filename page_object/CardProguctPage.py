from page_object.Base import BasePage
from selenium.webdriver.common.by import By


class CardProductPage(BasePage):
    BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    TAB_DESCRIPTION = (By.XPATH, "//a[@href='#tab-description']")
    TAB_REVIEW = (By.XPATH, "//a[@href='#tab-review']")
    PRODUCT_CODE = (By.XPATH, "//*[@id='content']//*[@class='list-unstyled']/li[1]")

    def check_existing_of_button_cart(self):
        return self._existing_of_elements(*self.BUTTON_CART)

    def check_existing_of_input_quantity(self):
        return self._existing_of_elements(*self.INPUT_QUANTITY)

    def check_existing_of_tab_description(self):
        return self._existing_of_elements(*self.TAB_DESCRIPTION)

    def check_existing_of_tab_review(self):
        return self._existing_of_elements(*self.TAB_REVIEW)

    def check_existing_of_product_code(self):
        return self._existing_of_elements(*self.PRODUCT_CODE)
