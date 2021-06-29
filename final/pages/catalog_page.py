from .base_page import BasePage
from .locators import CatalogPageLocators


class CatalogPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(CatalogPage, self).__init__(*args, **kwargs)

    def should_be_header_to_check(self):
        assert self.is_element_present(*CatalogPageLocators.HEAD_PAGE_LOCATOR), "Header on the page missed"

    def check_changed_language_on_header(self):
        caption_catalog = self.browser.find_element(*CatalogPageLocators.HEAD_PAGE_LOCATOR)

        assert caption_catalog.text == CatalogPageLocators.FRANCH_HEAD_PAGE_TEXT, \
            f"Text on the caption must be {CatalogPageLocators.FRANCH_HEAD_PAGE_TEXT}"

    def should_be_more_than_zero_items(self):
        items = self.browser.find_elements(*CatalogPageLocators.ITEMS_LIST_LOCATOR)
        assert len(items) > 0, "There are items in catalog"

    def check_item_card_info(self):
        assert self.is_element_present(*CatalogPageLocators.IMG_ITEM_LOCATOR), "Image of item is absent"
        assert self.is_element_present(*CatalogPageLocators.STAR_RATING_ITEM_LOCATOR), "Star rating is absent"
        assert self.is_element_present(*CatalogPageLocators.HEADER_ITEM_LOCATOR), "The name of item is absent"
        assert self.is_element_present(*CatalogPageLocators.PRICE_ITEM_LOCATOR), "The price of item is absent"
        assert self.is_element_present(*CatalogPageLocators.AVAILABILITY_ITEM_LOCATOR), "Availability field is absent"
        assert self.is_element_present(*CatalogPageLocators.BUTTON_ADD_ITEM_LOCATOR), "ADD button is absent"
