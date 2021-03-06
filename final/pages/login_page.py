from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "URL contain login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field is absent"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is absent"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is absent"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email field is absent"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Registration password field is absent"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION), "Registration password confirmation field is absent"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is absent"

    def register_new_user(self, email, password):
        new_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        new_email.send_keys(email)
        new_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        new_password.send_keys(password)
        new_password_confirmation = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION)
        new_password_confirmation.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button_registration.click()