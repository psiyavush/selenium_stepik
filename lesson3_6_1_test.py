import math
from setting import passport, email
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# создайте файл setting.py с двумя переменными passport и email (почта и пароль от stepik.org)
# корректировку времени производить здесь https://time.is/ru/
# и от этого изменять формулу math.log(int(time.time() + 0.5))


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    login_url = 'https://stepik.org'
    browser.get(login_url)
    log_btn = browser.find_element(By.XPATH, '/html/body/header/nav/a[2]')
    log_btn.click()
    enter_email = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
    enter_email.send_keys(email)
    enter_pas = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
    enter_pas.send_keys(passport)
    button = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
    button.click()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestStepikParametrize:
    link_list = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']

    @pytest.mark.parametrize('link', link_list)
    def test_stepik_parametrize(self, browser, link):
        url = f'https://stepik.org/lesson/{link}/step/1'
        browser.get(url)

        input_text = browser.find_element(By.XPATH, '//textarea')
        result = math.log(int(time.time() + 0.5))
        input_text.send_keys(result)

        button_send = browser.find_element(By.XPATH, '//button[text()="Отправить"]')
        button_send.click()

        text_result = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')
        assert 'Correct!' == text_result.text
        print('Test passed')
