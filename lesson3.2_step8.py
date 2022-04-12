"""
Cоставные сообщения об ошибках и поиск подстроки
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import sys

#assert "login" in browser.current_url, # сообщение об ошибке

def test_substring(full_string, substring):
    assert substring in full_string, "expected " + "'" +substring + "'" + " to be substring of " + "'" + full_string + "'"



# s = 'My Name is Julia'
#
# if 'Name' in s:
#     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')

# assert abs(-42) == -42, "Should be absolute value of a number"
#
# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result, "expected " + expected_result + ", got " + actual_result


# expected_result = 8
# actual_result = sys.stdin
# b = sys.stdout

# try:
#     browser = webdriver.Chrome()
#     browser.get(" http://suninjuly.github.io/explicit_wait2.html")
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     WebDriverWait(browser, 10).until(
#         EC.text_to_be_present_in_element((By.ID, "price"), "100")
#     )
#     browser.find_element(By.ID, "book").click()
#
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#     browser.find_element(By.ID, "answer").send_keys(y)
#     browser.find_element(By.ID, "solve").click()
#
# finally:
#     time.sleep(5)
#     browser.quit()