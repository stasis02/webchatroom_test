from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from conftest import wait
import testdata

class Asserts(wait):
    def __init__(self,driver):
        self.driver = driver

    def is_logged_in(self,test_n):
        expected_url = "http://127.0.0.1:8000/sign/undefined?member_name="
        WebDriverWait(self.driver, 3).until(EC.url_contains(expected_url))
        current_url = self.driver.current_url
        return current_url.startswith(expected_url)

    def is_meeting_created(self):
        try:
            expected_url = "http://127.0.0.1:8000/meeting"
            WebDriverWait(self.driver, 3).until(EC.url_contains(expected_url))
            current_url = self.driver.current_url
            return current_url.startswith(expected_url)
        except:
            return False

    def is_name_list_added(self,test_n):
        locator = (By.XPATH, '//*[@id="members"]/li')
        name_list = self.wait_for_elements_visibility(locator)
        if testdata.get_name(test_n) in [element.text for element in name_list]:
            return True
        else:
            return False

    def is_name_list_removed(self,test_n):
        locator = (By.XPATH, '//*[@id="members"]/li')
        name_list = self.wait_for_elements_visibility(locator)
        time.sleep(0.5)
        if testdata.get_name(test_n) not in [element.text for element in name_list]:
            return True
        else:
            return False

    def is_message_list_added(self,test_n):
        locator = (By.XPATH, '//*[@id="message-window"]/p')
        meeting_list = self.wait_for_elements_visibility(locator)
        if any(testdata.get_name(test_n) in element.text for element in meeting_list):
            return True
        else:
            return False

    def is_logged_out(self):
        expected_url = "http://127.0.0.1:8000"
        WebDriverWait(self.driver, 3).until(EC.url_contains(expected_url))
        current_url = self.driver.current_url
        return current_url.startswith(expected_url)
