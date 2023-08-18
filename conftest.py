import pytest

from selenium import webdriver
import testdata

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver.get(testdata.url)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver.get(testdata.url)
    yield driver
    driver.quit()


class wait:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visibility(self, locator: tuple):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element
        except:
            print('元素不可见')

    def wait_for_elements_visibility(self, locator: tuple):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_all_elements_located(locator))
            return element
        except:
            print('元素不可见')

    def wait_for_element_clickable(self, locator: tuple):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable(locator))
            return element
        except:
            print('元素不可点击')


