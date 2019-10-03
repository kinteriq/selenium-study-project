from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def _get_message(self, *args):
        self.browser.implicitly_wait(10)
        return self.browser.find_element(*args).text

    def add_to_basket_click(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        link.click()
    
    def correct_added_to_busket_book(self):
        title = self.browser.find_element(*ProductPageLocators.TITLE).text
        assert title == self._get_message(*ProductPageLocators.ADDED_TITLE),\
            "The title of added to basket book is incorrect"

    def correct_added_to_busket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price == self._get_message(*ProductPageLocators.TOTAL_PRICE),\
            "The price of added to basket book is incorrect"
    
    def should_be_login_link(self):
        pass

    def success_message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not dissapear"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is present, but should not be"