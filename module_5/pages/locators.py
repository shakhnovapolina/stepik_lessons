from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators():
    PRODUCT_BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    PRODUCT_ALERT_NAME_BOOK = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_HEADER_NAME_BOOK = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_ALERT_PRICE_BOOK = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    PRODUCT_BASKET_PRICE = (By.XPATH, "//div[contains(@class, 'basket-mini')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")


class BasketPageLocators():
    BASKET_LINK = (By.XPATH, "//a[contains(@href,'basket')]")
    BASKET_EMPTY_TEXT = (By.XPATH, "//div[@class='content']/div/p")
    BASKET_BOOK_IN_LIST = (By.XPATH, "//div[contains(@class,'basket-title')]/div/h2")
