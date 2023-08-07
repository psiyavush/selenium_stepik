# Фикстуры могут возвращать значение, которое затем можно использовать в тестах.
# Давайте перепишем наш предыдущий пример с использованием PyTest фикстур.
# Мы создадим фикстуру browser, которая будет создавать объект WebDriver.
# Этот объект мы сможем использовать в тестах для взаимодействия с браузером.
# Для этого мы напишем метод browser и укажем, что он является фикстурой с помощью декоратора @pytest.fixture.
# После этого мы можем вызывать фикстуру в тестах, передав ее как параметр.
# По умолчанию фикстура будет создаваться для каждого тестового метода, то есть для каждого теста запустится свой экземпляр браузера.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")