import pytest as pytest
import time

from test_assert import Asserts
from test_login import login
from test_meeting_create import MeetingCreate, MessageInput, MeetingLogout, MeetingJoin


def test_login(test_n,driver):
    login_instance = login(driver)
    login_instance.enter_usrname(test_n)
    login_instance.click_login(test_n)
    if test_n == 6:
        with pytest.raises(AssertionError):
            assert not Asserts(driver).is_logged_in(test_n)
    else:
        assert Asserts(driver).is_logged_in(test_n)

def test_login2(test_n,driver2):
    login_instance = login(driver2)
    login_instance.enter_usrname(test_n)
    login_instance.click_login(test_n)
    with pytest.raises(AssertionError):
        assert not Asserts(driver2).is_logged_in(test_n)


def test_create(test_n,driver):
    create_instance = MeetingCreate(driver)
    create_instance.enter_meeting_name(test_n)
    create_instance.click_create_m(test_n)
    if test_n == 6:
        assert not Asserts(driver).is_meeting_created()
    else:
        assert Asserts(driver).is_meeting_created()

def test_create2(test_n,driver2):
    create_instance = MeetingCreate(driver2)
    create_instance.enter_meeting_name(test_n)
    create_instance.click_create_m(test_n)
    assert not Asserts(driver2).is_meeting_created()

def test_name_list_add(test_n,driver):
    if test_n is not 6:
        assert Asserts(driver).is_name_list_added(test_n)
    else:
        pass

def test_name_list_remove(test_n,driver):
    if test_n is not 6:
        assert Asserts(driver).is_name_list_removed(test_n)
    else:
        pass

def test_input(test_n,driver):
    if test_n is not 6:
        message_instance = MessageInput(driver)
        message_instance.enter_message(test_n)
        message_instance.click_send(test_n)
    else:
        pass

def test_message_list_add(test_n,driver):
    if test_n is not 6:
        assert Asserts(driver).is_message_list_added(test_n)
    else:
        pass

def test_logout(test_n,driver):
    if test_n is not 6:
        logout_instance = MeetingLogout(driver)
        logout_instance.click_logout()
        assert Asserts(driver).is_logged_out()
    else:
        pass

def test_join(test_n,driver2):
    join_instance = MeetingJoin(driver2)
    join_instance.enter_meeting_name(test_n)
    join_instance.click_join_m(test_n)
    assert Asserts(driver2).is_meeting_created()


