import pytest
from selenium import webdriver
import logging
logging.basicConfig(level=logging.INFO, filename="logs/test_opencart_selenium.log")



def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://demo.opencart.com/", help="choose your url")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options_chr = webdriver.ChromeOptions()
        options_chr.add_argument('ignore-certificate-errors')
        # options_chr.headless = True
        driver = webdriver.Chrome(options=options_chr)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('ignore-certificate-errors')
        options.headless = True
        driver = webdriver.Firefox(firefox_options=options)
    else:
        raise Exception(f"{browser} is not supported!")

    driver.get(url)
    driver.implicitly_wait(3)
    driver.maximize_window()

    request.addfinalizer(driver.quit)

    return driver
