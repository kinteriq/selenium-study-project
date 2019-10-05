import time
import pytest

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
PROMO_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


@pytest.mark.basket_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        print('\n=======SETUP USER\n')
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        login_page.register_new_user(
            str(time.time()) + '@fakemail.org', 'lijhtfdwa')

        self.page = ProductPage(browser, PROMO_LINK)
        self.page.open()
       
    def test_user_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.page.add_to_basket_click()
        self.page.solve_quiz_and_get_code()

        self.page.correct_added_to_basket_book()
        self.page.correct_added_to_basket_price()


@pytest.mark.basket_guest
class TestGuestAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        print('\n=======SETUP GUEST\n')
        self.page = ProductPage(browser, PROMO_LINK)
        self.page.open()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self):
        self.page.add_to_basket_click()
        self.page.solve_quiz_and_get_code()

        self.page.correct_added_to_basket_book()
        self.page.correct_added_to_basket_price()

    def test_guest_cant_see_success_message_on_product_page(self):
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        self.page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        basket_page.basket_does_not_have_items()
        basket_page.basket_should_be_empty()

    @pytest.mark.xfail(strict=True)
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.page.add_to_basket_click()
        self.page.solve_quiz_and_get_code()

        self.page.should_not_be_success_message()

    @pytest.mark.xfail(strict=True)
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.page.add_to_basket_click()
        self.page.solve_quiz_and_get_code()

        self.page.success_message_should_dissapear()


@pytest.mark.login_guest
class TestGuestCanLoginFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        print('\n=======SETUP GUEST\n')
        self.page = ProductPage(browser, PROMO_LINK)
        self.page.open()
    
    def test_guest_should_see_login_link_on_product_page(self):
        self.page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.page.go_to_login_page()