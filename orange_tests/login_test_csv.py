from base.webdriver_wrapper import WebDriverWrapper
from orange_pages.login_page import LoginPage
from orange_pages.main_page import MainPage
from ddt import ddt, data, unpack
from utilities import read_data


@ddt
class Login1Test(WebDriverWrapper):

    @data(*read_data.get_csv_data("../data/orangehrm_py.csv"))
    # @data(("dina", "king","in"))
    @unpack
    def test_invalid_login(self, username, password, expectedtext):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        self.assertEqual(expectedtext, login.get_error_text())
