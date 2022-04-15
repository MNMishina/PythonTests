"""
Параметризация тестов
открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
"""
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLinks(unittest.TestCase):

    button = browser.find_element(By.CLASS_NAME, "submit-submission").click()

    text_answer = browser.find_element(By.CLASS_NAME, "smart-hints_hint").text

    assert text_answer == "Correct!" \
            f"Got{text_answer} instead of 'Correct'"
    @pytest.mark.parametrize('page_course', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


css_selector = 'cssSelectorForTestArea'
textarea_selector = (By.CSS_SELECTOR, css_selector)
WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable(textarea_selector))
textarea = browser.find_element(By.CSS_SELECTOR, css_selector)

answer = math.log(int(time.time()))



@pytest.mark.parametrize('link', ["WebDriverWait EC.visibility_of_element_located().text236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])

browser.implicity_wait(10)
send_key(str(math.log(int(time.time())))
WebDriverWait EC.element_to_be_clickable
WebDriverWait EC.visibility_of_element_located().text
def test_guest_should_see_login_link(browser, link):
    link = f"https://stepik.org/lesson/{link}"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    browser.find_element(By.CSS_SELECTOR, "#login_link")


if __name__ == "__main__":
    unittest.main()