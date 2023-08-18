import pytest as pytest
import test_modules


test_list = list(range(1,7))


@pytest.mark.skip(reason="单个用户测试已完成")
@pytest.mark.parametrize("test_n", test_list)
def test_main(test_n,driver):
    test_modules.test_login(test_n, driver)
    test_modules.test_create(test_n, driver)
    test_modules.test_name_list_add(test_n, driver)
    test_modules.test_input(test_n, driver)
    test_modules.test_message_list_add(test_n, driver)
    test_modules.test_logout(test_n, driver)

@pytest.mark.skip(reason="多个用户错误测试1已完成")
def test_chat_failed1(driver,driver2):
    test_modules.test_login(1, driver)
    test_modules.test_login2(1, driver2)

@pytest.mark.skip(reason="多个用户错误测试2已完成")
def test_chat_failed2(driver,driver2):
    test_modules.test_login(2, driver)
    test_modules.test_login(3, driver2)
    test_modules.test_create(2, driver)
    test_modules.test_create2(2, driver2)

def test_chat(driver,driver2):
    test_modules.test_login(4, driver)
    test_modules.test_login(5, driver2)
    test_modules.test_create(4, driver)
    test_modules.test_join(4, driver2)
    test_modules.test_name_list_add(5, driver)
    test_modules.test_name_list_add(4, driver2)
    test_modules.test_input(3, driver)
    test_modules.test_input(2, driver2)
    test_modules.test_message_list_add(3, driver2)
    test_modules.test_message_list_add(2, driver)
    test_modules.test_logout(4, driver)
    test_modules.test_name_list_remove(4, driver2)
    test_modules.test_logout(5, driver2)


if __name__ == '__main__':
    pytest.main()