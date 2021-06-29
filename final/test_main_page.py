import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


class TestMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_text_empty_basket()
        basket_page.check_cant_see_product_in_basket_opened()

    @pytest.mark.personal_tests
    @pytest.mark.parametrize('search_text', ["", "Hacking Work"])
    def test_find_item(self, browser, search_text):
        page = MainPage(browser, link)
        page.open()
        page.should_be_search_block()
        page.search_item(search_text)
        page.check_searched_item(search_text)

    @pytest.mark.personal_tests
    def test_welcom_text_on_start_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_welcome_text()
