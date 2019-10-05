import time
import pytest

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
PROMO_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.'


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        login_page.register_new_user(
            str(time.time()) + '@fakemail.org', 'lijhtfdwa')

        self.page = ProductPage(browser, PROMO_LINK)
        self.page.open()
       
    def test_user_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        self.page.add_to_basket_click()
        self.page.solve_quiz_and_get_code()

        self.page.correct_added_to_busket_book()
        self.page.correct_added_to_busket_price()


@pytest.mark.basket
@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PROMO_LINK)
    page.open()

    page.add_to_basket_click()
    page.solve_quiz_and_get_code()

    page.should_not_be_success_message()


@pytest.mark.basket
@pytest.mark.xfail(strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PROMO_LINK)
    page.open()

    page.add_to_basket_click()
    page.solve_quiz_and_get_code()

    page.success_message_should_dissapear()


@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PROMO_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PROMO_LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PROMO_LINK)
    page.open()
    page.go_to_basket_page()
    
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_does_not_have_items()
    basket_page.basket_should_be_empty()