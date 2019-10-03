from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_messages(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGES).text

    def add_to_basket_click(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        link.click()
    
    def added_to_basket_message_present(self):
        added_message = "has been added to your basket."
        assert added_message in self.get_messages(),\
            "No book is added message"
    
    def correct_added_to_busket_book(self):
        title = self.browser.find_element(*ProductPageLocators.TITLE).text
        assert title in self.get_messages(),\
            "The title of added to basket book is incorrect"
        
    def total_price_message_present(self):
        total_price_message = "Your basket total is"
        assert total_price_message in self.get_messages(),\
            "No total price message"

    def correct_added_to_busket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price in self.get_messages(),\
            "The price of added to basket book is incorrect"
