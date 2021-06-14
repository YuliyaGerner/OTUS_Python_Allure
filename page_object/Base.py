from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("поиск элемента на странице")
    def __element(self, *locator, index=0):
        self.logger.info("Search of element {} with index {}".format(locator[1], index))
        return self.driver.find_elements(*locator)[index]

    @allure.step("проверка наличия элемента на странице")
    def _existing_of_elements(self, *locator, count_of_elements=1):
        self.logger.info("Check existing of {} element(s) {}".format(count_of_elements, locator[1]))
        return len(self.driver.find_elements(*locator)) == count_of_elements

    @allure.step("клик по элементу")
    def _click(self, *locator):
        self.logger.info("Click element {}".format(locator[1]))
        ActionChains(self.driver).move_to_element(self.__element(*locator)).click().perform()

    @allure.step("ожидание видимости элемента на странице")
    def _wait_for_visible(self, *locator, wait=5):
        self.logger.info("Wait for element {} during {} seconds".format(locator[1], wait))
        element = self.driver.find_element(*locator)
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(element))

    @allure.step("переход по ссылке")
    def _open(self, url, path=''):
        self.logger.info("Open url {}{}".format(url, path))
        target_url = url + path
        self.driver.get(target_url)
