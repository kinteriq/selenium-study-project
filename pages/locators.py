from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,
        "a[class='btn btn-default'][href$='basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div[id='content_inner'] p")
    BASKET_CONTENT = (By.CSS_SELECTOR,
        "div[class='basket-items'] div[class='row']")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_BTN = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR,
        "form[id='add_to_basket_form'] button[class$='btn-add-to-basket']")
    TITLE = (By.CSS_SELECTOR, "div[class$='product_main'] h1")
    PRICE = (By.CSS_SELECTOR, "div[class$='product_main'] p[class='price_color']")
    ADDED_TITLE = (By.CSS_SELECTOR,
        "div[class='alert alert-safe alert-noicon alert-success  fade in'] strong")
    TOTAL_PRICE = (By.CSS_SELECTOR,
    "div[class='alert alert-safe alert-noicon alert-info  fade in'] strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[id='messages'] div[class='alertinner ']")