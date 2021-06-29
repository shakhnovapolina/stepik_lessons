import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', help="Choose language: ru, en-GB, fr, es. Default: en-GB",
                     default="en-GB")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    param_lang_browser = webdriver.ChromeOptions()
    # disabled usb-spam logs
    param_lang_browser.add_experimental_option("excludeSwitches", ["enable-logging"])
    param_lang_browser.add_experimental_option('prefs', {'intl.accept_languages': language})

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=param_lang_browser)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=param_lang_browser)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
