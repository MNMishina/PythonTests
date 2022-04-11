"""
execute_script
Считать значение для переменной x
Посчитать математическую функцию от x
Проскроллить страницу вниз
Ввести ответ в текстовое поле
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!"
Нажать на кнопку "Submit"
"""
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    # browser.execute_script("document.getElementById('IDName')")
    # style.display = 'none' скрывает футер
    browser.execute_script("document.querySelector('footer.bd-footer.bg-light.text-muted').style.display = 'none';")
    # browser.execute_script("window.scrollBy(0, 100);")  прокрутка на 100 пикселей вниз

    browser.find_element(By.ID, "answer").send_keys(y)

    #browser.find_element(By.ID, "robotCheckbox").click         # инструкция не сработала
    browser.execute_script("document.getElementById('robotCheckbox').click();")
    #browser.find_element(By.ID, "robotsRule").click            # инструкция не сработала
    browser.execute_script("document.getElementById('robotsRule').click();")
    #browser.find_element(By.CSS_SELECTOR, "button.btn").click() # инструкция не сработала
    browser.execute_script("document.querySelector('button.btn').click();")

    # browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)   можно скрывать ненужный элемент

finally:
    time.sleep(10)
    browser.quit()