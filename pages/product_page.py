from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def _get_book_title(self):
        return self.browser.find_element(*ProductPageLocators.TITLE).text
    
    def _get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def _get_message(self, *args):
        return self.browser.find_element(*args).text

    def add_to_basket_click(self):
        link = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BTN)
        link.click()
    
    def correct_added_to_basket_book(self):
        title = self._get_book_title()
        added_title = self._get_message(*ProductPageLocators.ADDED_TITLE)
        assert title == added_title,\
            f'''The title of added to basket book is incorrect: \
                "{added_title}" instead of "{title}"'''

    def correct_added_to_basket_price(self):
        price = self._get_book_price()
        added_price = self._get_message(*ProductPageLocators.TOTAL_PRICE)
        assert price == added_price,\
            f'''The price of added to basket book is incorrect: \
                "{added_price}" instead of "{price}"'''

    def success_message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message did not dissapear'
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
                'Success message is present, but should not be'