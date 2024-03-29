"""*
* поиск элемента по тексту в ссылке
*"""

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link1 = "https://www.degreesymbol.net/"
link2 = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    #link1 = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
    link2 = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link2.click()
    print(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    input1 = browser.find_element(By.TAG_NAME, "input.form-control")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
