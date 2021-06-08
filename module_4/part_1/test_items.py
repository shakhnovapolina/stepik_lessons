link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
lang = {"ru": "Добавить в корзину", "en": "Add to basket", "es": "Añadir al carrito", "fr": "Ajouter au panier"}
button_add_backet_locator = "button.btn-add-to-basket"
droplist_language_option_locator = '//option[@selected="selected"]'

def test_check_language(browser):
    # Arrange
    browser.get(link)

    # Act
    button_add_backet = browser.find_element_by_css_selector(button_add_backet_locator)
    droplist_language_option = browser.find_element_by_xpath(droplist_language_option_locator)
    selected_language = droplist_language_option.get_attribute("value")

    # Assert
    assert button_add_backet.text == lang[selected_language]
