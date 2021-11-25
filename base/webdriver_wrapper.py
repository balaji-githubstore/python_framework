import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class WebDriverWrapper(unittest.TestCase):
    driver=None

    def setUp(self):
        s = Service(executable_path="C:\\Components\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.maximize_window()



    def tearDown(self):
        self.driver.quit()
