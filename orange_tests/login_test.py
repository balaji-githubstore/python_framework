import unittest

import HtmlTestRunner

from base.webdriver_wrapper import WebDriverWrapper
from orange_pages.login_page import LoginPage
from orange_pages.main_page import MainPage
from ddt import ddt, data, unpack


@ddt
class LoginTest(WebDriverWrapper):

    def test_valid_login(self):
        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        main = MainPage(self.driver)
        self.assertEqual("My Info", main.get_my_info_text())

    @data(("bala", "dina"),("dina", "king"))
    @unpack
    def test_invalid_login(self, username, password):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        self.assertEqual("Invalid credentials", login.get_error_text())
