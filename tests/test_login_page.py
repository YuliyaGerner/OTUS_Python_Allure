from page_object.LoginPage import LoginPage
import allure


@allure.title("Проверка наличия основных элементов на странице логина")
def test_on_login_page(browser, url):
    login_url = url + '/index.php?route=account/login'
    browser.get(login_url)
    LoginPage(browser).check_existing_of_registration_button()
    LoginPage(browser).check_existing_of_email_input()
    LoginPage(browser).check_existing_of_password_input()
    LoginPage(browser).check_existing_of_login_button()
    LoginPage(browser).check_existing_of_forgotten_password_button()
