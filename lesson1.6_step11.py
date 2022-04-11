"""*
* Заполнение обязательных полей при регистрации - неуспешный тест: NoSuchElementException из-за отсутствия поля Last name
*"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input1.send_keys("Rita")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")  # Исчезло обязательное поле Last name
    input2.send_keys("Bogatova")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    input2.send_keys("uspeh@kruto.com")
    time.sleep(3)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()