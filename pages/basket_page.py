from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        content = self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert content.startswith('Your basket is empty.'),\
            'Basket is not empty'
    
    def basket_does_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT),\
            'Basket is empty but should not be'
