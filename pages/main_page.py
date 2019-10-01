from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK),\
            "Login link is not presented"
    
    def should_be_login_url(self):
        assert "login" in self.browser.current_url,\
            "Not a login url"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM),\
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM),\
            "Registration form is not presented"