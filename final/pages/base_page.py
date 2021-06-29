import math

from selenium.webdriver.support.select import Select

from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_languages_selector(self):
        assert self.is_element_present(
            *BasePageLocators.DROPDOWN_LANGUAGE_LOCATOR), "Dropdown list to change language missed"
        assert self.is_element_present(*BasePageLocators.BUTTON_LANGUAGE_LOCATOR), "Button to change language missed"

    def opened_language_not_like_new(self):
        search_dropdown = Select(self.browser.find_element(*BasePageLocators.DROPDOWN_LANGUAGE_LOCATOR))
        assert search_dropdown.all_selected_options != BasePageLocators.NEW_LANG_OPTION, "Browser already has been opened in new lang"

    def change_language(self):
        search_dropdown = Select(self.browser.find_element(*BasePageLocators.DROPDOWN_LANGUAGE_LOCATOR))
        search_dropdown.select_by_value(BasePageLocators.NEW_LANG_OPTION)
        button_confirm_lang = self.browser.find_element(*BasePageLocators.BUTTON_LANGUAGE_LOCATOR)
        button_confirm_lang.click()

    def check_changed_language_on_button_lang_confirm(self):
        button_confirm_lang = self.browser.find_element(*BasePageLocators.BUTTON_LANGUAGE_LOCATOR)
        assert button_confirm_lang.text == BasePageLocators.FRANCH_TEXT_BUTTON, \
            f"Text on button must be {BasePageLocators.FRANCH_TEXT_BUTTON}"

    def should_be_search_block(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_FIELD_LOCATOR), "Field to search is absent"
        assert self.is_element_present(*BasePageLocators.SEARCH_BUTTON_LOCATOR), "Button to search is absent"

    def search_item(self, search_text):
        search_field = self.browser.find_element(*BasePageLocators.SEARCH_FIELD_LOCATOR)
        search_field.send_keys(search_text)
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON_LOCATOR)
        search_button.click()

    def check_searched_item(self, search_text):
        result_header = self.browser.find_element(*BasePageLocators.HEADER_PAGE_SEARCHED)
        assert search_text in result_header.text, "Search text was not apply"


