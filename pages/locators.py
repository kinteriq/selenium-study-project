from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    BasePage.is_element_present(how, what)
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "form[id='add_to_basket_form'] \
        button[class$='btn btn-lg btn-primary btn-add-to-basket']")
    TITLE = (By.CSS_SELECTOR, "div[class$='product_main'] h1")
    PRICE = (By.CSS_SELECTOR, "div[class$='product_main'] p[class='price_color']")
    MESSAGES = (By.CSS_SELECTOR, "div[id='messages'],div[class='alertinner']")