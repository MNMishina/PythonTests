import pytest

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

# @pytest.mark.flaky(reruns=2) #указываем кол-во перезапусков
# def test_guest_should_see_login_link_fail(browser):
#     browser.get(link)
#     browser.find_element_by_css_selector("#magic_link")