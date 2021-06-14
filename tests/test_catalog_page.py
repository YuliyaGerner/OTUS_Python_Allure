from page_object.CatalogPage import CatalogPage
import allure


@allure.title("Проверка наличия основных элементов на странице каталога")
def test_on_catalog_page(browser, url):
    catalog_url = url + '/index.php?route=product/category&path=20'
    browser.get(catalog_url)
    CatalogPage(browser).check_existing_of_list_view_element()
    CatalogPage(browser).check_existing_of_add_to_cart_button()
    CatalogPage(browser).check_existing_of_sort_input()
    CatalogPage(browser).check_existing_of_limit_input()
    CatalogPage(browser).check_existing_of_price()
