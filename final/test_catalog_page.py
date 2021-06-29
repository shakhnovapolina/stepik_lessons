import pytest

from final.pages.catalog_page import CatalogPage

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'


@pytest.mark.personal_tests
class TestCatalogPage:

    def test_change_language(self, browser):
        page = CatalogPage(browser, link)
        page.open()
        page.should_be_languages_selector()
        page.opened_language_not_like_new()
        page.change_language()
        page.should_be_languages_selector()
        page.should_be_header_to_check()
        page.check_changed_language_on_button_lang_confirm()
        page.check_changed_language_on_header()

    def test_more_than_zero_items_in_catalogue(self, browser):
        page = CatalogPage(browser, link)
        page.open()
        page.should_be_more_than_zero_items()

    def test_items_card_is_fulled(self, browser):
        page = CatalogPage(browser, link)
        page.open()
        page.check_item_card_info()

