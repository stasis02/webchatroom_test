
from selenium.webdriver.common.by import By
from conftest import wait
import testdata






class login(wait):
    # 输入用户名
    def enter_usrname(self, test_n):
        locator = (By.ID, 'username')
        username_element = self.wait_for_element_visibility(locator)
        username_element.send_keys(testdata.get_name(test_n))
    # 点击登录按钮
    def click_login(self, test_n):
        locator= (By.XPATH, '//*[@id="login-form"]/button')
        login_button = self.wait_for_element_clickable(locator)
        login_button.click()


