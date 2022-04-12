"""
Тесты оформляем в стиле unittest
"""
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By

class TestRegistry(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_reg1(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input1.send_keys("Rita")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")  # Исчезло обязательное поле Last name
        input2.send_keys("Bogatova")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        input2.send_keys("uspeh@kruto.com")
        time.sleep(1)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        time.sleep(1)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong text has been displayed")

    def test_reg2(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input1.send_keys("Rita")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")  # Исчезло обязательное поле Last name
        input2.send_keys("Bogatova")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        input2.send_keys("uspeh@kruto.com")
        time.sleep(1)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        time.sleep(1)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong text has been displayed")

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")