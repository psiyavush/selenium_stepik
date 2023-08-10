import pytest
from selenium import webdriver
# Встроенная фикстура request и встроенная функция pytest_addoption
# позволяют настраивать тестовые окружения с помощью передачи параметров через командную строку
# Добавим логику обработки командной строки по выбору браузера для теста (chrome or firefox)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# Если вы теперь запустите тесты без параметра, то получите ошибку:
# pytest -s -v test_parser.py
# нужно: pytest -s -v --browser_name=chrome test_parser.py
# или: pytest -s -v --browser_name=firefox test_parser.py
# можно задать значение по умолчанию:
# parser.addoption('--browser_name', action='store', default="chrome",
#                  help="Choose browser: chrome or firefox")