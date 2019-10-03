import time

from pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.'
# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket_click()
    page.solve_quiz_and_get_code()

    page.added_to_basket_message_present()
    page.correct_added_to_busket_book()

    page.total_price_message_present()
    page.correct_added_to_busket_price()