import pytest

from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_submit_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button')

    assert len(button) > 0, 'Элемент button не найден'
    print("Элемент button успешно найден")


if __name__ == '__main__':
    pytest.test_items()

# Запуск для проверки
# pytest --language=es test_items.py
# pytest --language=fr test_items.py