from selenium import webdriver

import unittest

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080")

    def test_titulo(self):
        self.assertEqual(self.driver.title, "DevSecOps")        

    def tearDown(self) -> None:
        self.driver.close()