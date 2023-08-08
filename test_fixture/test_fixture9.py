# PyTest позволяет запустить один и тот же тест с разными входными параметрами.
# Для этого используется декоратор @pytest.mark.parametrize()
# Наш сайт доступен для разных языков. Напишем тест, который проверит, что для сайта
# с русским и английским языком будет отображаться ссылка на форму логина.
# Передадим в наш тест ссылки на русскую и английскую версию главной страницы сайта.

# В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться,
# и список значений параметра. В самом тесте наш параметр тоже нужно передавать в качестве аргумента.
# Обратите внимание, что внутри декоратора имя параметра оборачивается в кавычки,
# а в списке аргументов теста кавычки не нужны.

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

# Запуск - pytest -s -v test_fixture9.py