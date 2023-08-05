from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[1]")
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    input3.send_keys('i_petrov@mail.test')
    current_dir = os.path.abspath(os.path.dirname("lesson2.2_3.py"))
    file_path = os.path.join(current_dir, 'test.txt')
    input4 = browser.find_element(By.XPATH, '//*[@id="file"]')
    input4.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


