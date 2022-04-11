"""
Работа с выпадающим списком
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
link1 = "http://suninjuly.github.io/selects2.html" # видна часть выпадающего списка
try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.ID, "num1")
    a = a_element.text
    b_element = browser.find_element(By.ID, "num2")
    b = b_element.text
    c = int(a)+int(b)
    #c = str(int(a)+int(b))
    print(a, "+", b, "=", c)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(c))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    browser.quit()