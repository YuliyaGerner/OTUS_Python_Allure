from page_object.Base import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    admin_page_path = '/admin'
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.XPATH, "//*[@type = 'submit']")
    FORGOTTEN_PASSWORD_BUTTON = (By.LINK_TEXT, "Forgotten Password")
    LOGO = (By.CSS_SELECTOR, "#header-logo")
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "#button-setting")
    TITLE_OF_SETTINGS_MODAL_WINDOW = (By.XPATH, "//*[@class='modal-title']")
    CALENDAR_of_SALES_ANALYTICS_BLOCK = (By.XPATH, "//div/a[@class='dropdown-toggle']")
    DROP_DOWN_MENU_OF_SALES_ANALYTICS_BLOCK = (By.XPATH, "//*[@id='range']")
    NAVIGATION_TITLE = (By.CSS_SELECTOR, "#navigation")
    USER_NAME_DEMO = (By.XPATH, "//*[@alt='demo demo']")
    LOGOUT_BUTTON = (By.XPATH, "//*[@id='header']/div/ul/li[2]/a")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCT_MENU = (By.XPATH, "//*[@id='menu-catalog']/ul[1]/li[2]")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")

    def open_admin_page(self, url):
        return self._open(url, self.admin_page_path)

    def admin_page_check_existing_of_username_input(self):
        return self._existing_of_elements(*self.USERNAME_INPUT)

    def admin_page_check_existing_of_password_input(self):
        return self._existing_of_elements(*self.PASSWORD_INPUT)

    def admin_page_check_existing_of_login_button(self):
        return self._existing_of_elements(*self.LOGIN_BUTTON)

    def admin_page_check_existing_of_forgotten_password_button(self):
        return self._existing_of_elements(*self.FORGOTTEN_PASSWORD_BUTTON)

    def admin_page_check_existing_of_logo(self):
        return self._existing_of_elements(*self.LOGO)

    def click_on_login_button(self):
        return self._click(*self.LOGIN_BUTTON)

    def wait_for_logo_on_login_page(self):
        return self._wait_for_visible(*self.LOGO)

    def click_on_settings_button(self):
        return self._click(*self.SETTINGS_BUTTON)

    def check_existing_of_title_setting_modal_window(self):
        return self._existing_of_elements(*self.TITLE_OF_SETTINGS_MODAL_WINDOW)

    def click_on_calendar(self):
        return self._click(*self.CALENDAR_of_SALES_ANALYTICS_BLOCK)

    def check_existing_of_drop_down_calendar_menu(self):
        return self._existing_of_elements(*self.DROP_DOWN_MENU_OF_SALES_ANALYTICS_BLOCK)

    def wait_for_navigation_title_on_admin_page(self):
        return self._wait_for_visible(*self.NAVIGATION_TITLE)

    def check_existing_of_demo_login(self):
        return self._existing_of_elements(*self.USER_NAME_DEMO)

    def click_on_logout_button(self):
        return self._click(*self.LOGOUT_BUTTON)

    def click_on_catalog_menu(self):
        return self._click(*self.MENU_CATALOG)

    def click_on_product_menu(self):
        return self._click(*self.PRODUCT_MENU)

    def check_existing_of_products_link(self):
        return self._existing_of_elements(*self.PRODUCTS_LINK)

    def go_to_admin_page(self, url):
        self.open_admin_page(url)
        self.wait_for_logo_on_login_page()
        self.click_on_login_button()
        self.wait_for_navigation_title_on_admin_page()
