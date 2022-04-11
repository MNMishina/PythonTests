"""
Загрузка файла
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
"""
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"
#path = os.getcwd() + '/' + 'Lesson2.2step8.txt'

# directory = "C:/Users/exist/PycharmProjects/autoTests/"
# file_name = "Lesson2.2step8.txt"
# file_path = os.path.join(directory, file_name)

#current_dir = os.path.abspath(os.path.dirname(C:/Users/exist/PycharmProjects/autoTests/))  # получаем путь к директории текущего исполняемого файла
#file_path = os.path.join(current_dir, 'Lesson2.2step8.txt')  # добавляем к этому пути имя файла

        # получаем путь к директории текущего исполняемого скрипта lesson2.2_step8.py
current_dir = os.path.abspath(os.path.dirname(__file__))
        # имя файла, который будем загружать на сайт
file_name = "Lesson2.2step8.txt"
        # получаем путь к file_example.txt ("Lesson2.2step8")
file_path = os.path.join(current_dir, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("123@mail.ru")

    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(7)
    browser.quit()