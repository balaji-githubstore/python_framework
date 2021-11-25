import unittest


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("class teardown")

    def setUp(self):
        print("run setup")

    def tearDown(self) -> None:
        print("run teardown")

    def test_valid_login(self):
        print("valid")

    def test_invalid_login(self):
        print("invalid")
