from page_object.CardProguctPage import CardProductPage
import allure


@allure.title("Проверка наличия основных элементов на странице товара")
def test_on_product_page(browser, url):
    phone_url = url + '/index.php?route=product/product&path=57&product_id=49'
    browser.get(phone_url)
    CardProductPage(browser).check_existing_of_button_cart()
    CardProductPage(browser).check_existing_of_input_quantity()
    CardProductPage(browser).check_existing_of_tab_description()
    CardProductPage(browser).check_existing_of_tab_review()
    CardProductPage(browser).check_existing_of_product_code()
