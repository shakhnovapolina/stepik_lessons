import pytest
from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestProductPage:

    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        page = ProductPage(browser,
                        link + '/?promo=' + promo_offer)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_backet()
        page.solve_quiz_and_get_code()
        page.check_add_book_alert()
        page.check_price_book_basket()

