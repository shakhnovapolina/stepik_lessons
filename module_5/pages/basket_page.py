from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_text_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT), "Text about empty basket is not presented"

    def check_cant_see_product_in_basket_opened(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_BOOK_IN_LIST), \
            "Success message is presented, but should not be"
