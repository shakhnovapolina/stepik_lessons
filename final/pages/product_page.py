from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_BUTTON_ADD_TO_BASKET), "Button Add-to-Basket is not presented"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_name_book_in_alert(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_ALERT_NAME_BOOK), "Name of book in alert is not presented"

    def should_be_name_book_product_page(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_HEADER_NAME_BOOK), "Name of book on the product page is not presented"

    def check_add_book_alert(self):
        alert_name_book = self.browser.find_element(*ProductPageLocators.PRODUCT_ALERT_NAME_BOOK).text
        header_name_book = self.browser.find_element(*ProductPageLocators.PRODUCT_HEADER_NAME_BOOK).text
        assert alert_name_book == header_name_book, "Different names of book in the basket and was added"

    def should_be_price_in_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ALERT_PRICE_BOOK), "Price on alert is not presented"

    def should_be_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BASKET_PRICE), "Price on basket is not presented"

    def check_price_book_basket(self):
        basket_price_book = \
        self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE).text.split('\n')[0].split(':')[1].strip()
        alert_price_book = self.browser.find_element(*ProductPageLocators.PRODUCT_ALERT_PRICE_BOOK).text.strip()
        assert basket_price_book == alert_price_book, (
            f"Different prices -{basket_price_book}- and alert -{alert_price_book}-")

    def check_success_message_is_not_element(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_is_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
