from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    # change language to fr
    DROPDOWN_LANGUAGE_LOCATOR = (By.XPATH, "//select[@name=\"language\"]")
    BUTTON_LANGUAGE_LOCATOR = (By.XPATH, "//button[@class=\"btn btn-default\"]")
    NEW_LANG_OPTION = "fr"
    FRANCH_TEXT_BUTTON = "Envoyer"
    SEARCH_FIELD_LOCATOR = (By.XPATH, "//input[@type='search']")
    SEARCH_BUTTON_LOCATOR = (By.XPATH, "//input[@type='submit']")
    HEADER_PAGE_SEARCHED = (By.XPATH, "//h1")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    WELCOME_BLOCK = (By.XPATH, "//section[contains(@class, 'well')]")


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


class CatalogPageLocators():
    FRANCH_HEAD_PAGE_TEXT = "Tous les produits"
    HEAD_PAGE_LOCATOR = (By.XPATH, "//div[@class=\"page-header action\"]/h1")
    ITEMS_LIST_LOCATOR = (By.XPATH, "//article[@class='product_pod']")
    IMG_ITEM_LOCATOR = (By.XPATH, "//article[@class='product_pod']//img")
    STAR_RATING_ITEM_LOCATOR = (By.XPATH, "//article[@class='product_pod']//p")
    HEADER_ITEM_LOCATOR = (By.XPATH, "//article[@class='product_pod']//h3")
    PRICE_ITEM_LOCATOR = (By.XPATH, "//article[@class='product_pod']//div/p[@class='price_color']")
    AVAILABILITY_ITEM_LOCATOR = (By.XPATH, "//article[@class='product_pod']//p[@class='instock availability']")
    BUTTON_ADD_ITEM_LOCATOR = (By.XPATH, "//article[@class='product_pod']//button")

