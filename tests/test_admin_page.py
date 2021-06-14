from page_object.AdminPage import AdminPage
import allure


@allure.title("Проверка наличия основных элементов на странице администрирования")
@allure.description(
    """Список проверяемых элементов:
     - поле ввода username,
     - поле ввода пароля,
     - кнопка логина,
     - кнопка для восстановления пароля,
     - логотип""")
def test_existing_elements_on_admin_page(browser, url):
    admin_p = AdminPage(browser)
    admin_p.open_admin_page(url)
    admin_p.admin_page_check_existing_of_username_input()
    admin_p.admin_page_check_existing_of_password_input()
    admin_p.admin_page_check_existing_of_login_button()
    admin_p.admin_page_check_existing_of_forgotten_password_button()
    admin_p.admin_page_check_existing_of_logo()
    allure.dynamic.title("Все основные элементы присутствуют на странице администрирования")


@allure.title("Проверка наличия модального окна на странице администрирования")
def test_check_settings_modal_window_on_admin_page(browser, url):
    admin_p = AdminPage(browser)
    admin_p.go_to_admin_page(url)
    admin_p.click_on_settings_button()
    admin_p.check_existing_of_title_setting_modal_window()


@allure.title("Проверка наличия календаря в блоке аналитики продаж на странице администрирования")
def test_check_calendar_on_sales_analytics_block_on_admin_page(browser, url):
    admin_p = AdminPage(browser)
    admin_p.go_to_admin_page(url)
    admin_p.click_on_calendar()
    admin_p.check_existing_of_drop_down_calendar_menu()


@allure.feature('Authorization')
@allure.title("Проверка валидных login и logout на странице администрирования")
def test_check_demo_login_and_logout_on_admin_page(browser, url):
    admin_p = AdminPage(browser)
    admin_p.go_to_admin_page(url)
    admin_p.check_existing_of_demo_login()
    admin_p.click_on_logout_button()
    admin_p.wait_for_logo_on_login_page()
    admin_p.admin_page_check_existing_of_logo()


@allure.title("Проверка наличия таблицы с товарами на странице администрирования")
def test_check_product_table(browser, url):
    admin_p = AdminPage(browser)
    admin_p.go_to_admin_page(url)
    admin_p.click_on_catalog_menu()
    admin_p.click_on_product_menu()
    admin_p.check_existing_of_products_link()
