from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080")

    def test_titulo(self):
        self.assertEqual(self.driver.title, "DevSecOps")

    def test_cabecalho(self):
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "Olá, mundo!")      

    def tearDown(self) -> None:
        self.driver.close()