import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",  # задан chrome по умолчанию
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="es",
                     help="Choose language: en, es, ru...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nЗапуск браузер Chrome для теста...")
        options = OptionsChrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nЗапуск браузер Firefox для теста...")
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name должно быть chrome или firefox")
    yield browser
    print("\nЗакрыть браузер...")
    browser.quit()
