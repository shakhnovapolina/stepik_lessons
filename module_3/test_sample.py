from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
search_dropdown_locator = "//select[@name=\"language\"]"
search_button_lang_locator = "//button[@class=\"btn btn-default\"]"


def change_language():
    # Data
    lang_option = "fr"
    search_h1_locator = "//div[@class=\"page-header action\"]/h1"
    franch_text_button = "Envoyer"
    franch_text_h1 = "Tous les produits"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        search_dropdown = Select(browser.find_element_by_xpath(search_dropdown_locator))
        assert search_dropdown.all_selected_options != lang_option

        # Act
        search_dropdown.select_by_value(lang_option)
        button_confirm_lang = browser.find_element_by_xpath(search_button_lang_locator)
        button_confirm_lang.click()

        # Assert
        button_confirm_lang = browser.find_element_by_xpath(search_button_lang_locator)
        assert button_confirm_lang.text == franch_text_button, \
            f"Text on button must be -- {franch_text_button} --"

        caption_catalog = browser.find_element_by_xpath(search_h1_locator)
        assert caption_catalog.text == franch_text_h1, \
            f"Text on the caption must be -- {franch_text_h1} --"

    finally:
        browser.quit()


change_language()
