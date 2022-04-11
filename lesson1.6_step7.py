"""
использование метода find_elements_by
"""
from selenium import webdriver
import time
import random # модуль для рандомных чисел
import string # модуль для строк
from selenium.webdriver.common.by import By

try:
    letters = string.ascii_lowercase # Создаем строку из букв англ. алфавита в нижнем регистре
    browser = webdriver.Chrome()
    #browser.maximize_window()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        random_word = ''.join(random.choice(letters) for _ in range(8)) # В цикл добавляем генерацию случайного набора символов (диапазон произвольный)
        element.send_keys(random_word) # в цикле заполняем поле этим словом
        #element.send_keys("Тест1234")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    #alert = browser.switch_to_alert()
    #print(alert.text)

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла