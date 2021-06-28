import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.login
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "20210616"
        login_page = LoginPage(browser,
                               url)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()  # открываем страницу
        login_page.should_be_register_form()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_basket()
        page.check_add_book_alert()
        page.check_price_book_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.check_success_message_is_not_element()


class TestProductPage():
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        page = ProductPage(browser,
                           link + '/?promo=' + promo_offer)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_add_book_alert()
        page.check_price_book_basket()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.check_success_message_is_not_element()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_success_message_is_not_element()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_success_message_is_dissapear()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_text_empty_basket()
        basket_page.check_cant_see_product_in_basket_opened()
