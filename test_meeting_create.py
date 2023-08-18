from selenium.webdriver.common.by import By
import testdata
from conftest import wait


class MeetingCreate(wait):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_meeting_name(self, test_n):
        locator = (By.ID, 'meetingname')
        element = self.wait_for_element_visibility(locator)
        element.send_keys(testdata.get_name_m(test_n))

    def click_create_m(self,test_n):
        locator = (By.ID, 'create-button')
        element = self.wait_for_element_clickable(locator)
        element.click()


class MeetingJoin(wait):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_meeting_name(self, test_n):
        locator = (By.ID, 'meetingname')
        element = self.wait_for_element_visibility(locator)
        element.send_keys(testdata.get_name_m(test_n))

    def click_join_m(self,test_n):
        locator = (By.ID, 'enter-button')
        element = self.wait_for_element_clickable(locator)
        element.click()

class MessageInput(wait):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_message(self, test_n):
        locator = (By.ID, 'message-input')
        element = self.wait_for_element_visibility(locator)
        element.send_keys(testdata.get_name(test_n))

    def click_send(self,test_n):
        locator = (By.ID, 'send-button')
        element = self.wait_for_element_clickable(locator)
        element.click()

class MeetingLogout(wait):
    def __init__(self, driver):
        super().__init__(driver)

    def click_logout(self):
        locator = (By.ID, 'leave-button')
        element = self.wait_for_element_clickable(locator)
        element.click()