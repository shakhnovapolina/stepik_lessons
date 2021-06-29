from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_welcome_text(self):
        assert self.browser.find_elements(
            *MainPageLocators.WELCOME_BLOCK), "There are no welcome-block on the main page"
