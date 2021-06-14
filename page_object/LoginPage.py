from page_object.Base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    REGISTRATION_BUTTON = (By.LINK_TEXT, "Continue")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.XPATH, "//*[@value = 'Login']")
    FORGOTTEN_PASSWORD_BUTTON = (By.LINK_TEXT, "Forgotten Password")

    def check_existing_of_registration_button(self):
        return self._existing_of_elements(*self.REGISTRATION_BUTTON)

    def check_existing_of_email_input(self):
        return self._existing_of_elements(*self.EMAIL_INPUT)

    def check_existing_of_password_input(self):
        return self._existing_of_elements(*self.PASSWORD_INPUT)

    def check_existing_of_login_button(self):
        return self._existing_of_elements(*self.LOGIN_BUTTON)

    def check_existing_of_forgotten_password_button(self):
        return self._existing_of_elements(*self.FORGOTTEN_PASSWORD_BUTTON)
