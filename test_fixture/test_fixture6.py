# Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks).
# Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name — произвольная строка.
# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
# pytest -s -v -m smoke test_fixture6.py
# Не забудь регистрировать метки
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
