import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


LINK = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)
    page.open()

    page.should_be_login_link()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, LINK)
    page.open()

    page.should_be_basket_link()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_does_not_have_items()
    basket_page.basket_should_be_empty()