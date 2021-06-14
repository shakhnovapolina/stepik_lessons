import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', help="Choose language: ru, en-GB, fr, es. Default: en-GB",
                     default="en-GB")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    param_lang_browser = webdriver.ChromeOptions()
    param_lang_browser.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=param_lang_browser)
    yield browser
    print("\nquit browser..")
    browser.quit()
