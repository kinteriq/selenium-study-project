import pytest

from pages.product_page import ProductPage
from pages.basket_page import BasketPage


LINKS = [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.',
    "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/",
]


@pytest.mark.basket
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket_click()
    page.solve_quiz_and_get_code()

    page.correct_added_to_busket_book()
    page.correct_added_to_busket_price()


@pytest.mark.basket
@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINKS[0])
    page.open()

    page.add_to_basket_click()
    page.solve_quiz_and_get_code()

    page.should_not_be_success_message()


@pytest.mark.basket
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINKS[0])
    page.open()
    page.should_not_be_success_message()


@pytest.mark.basket
@pytest.mark.xfail(strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINKS[0])
    page.open()

    page.add_to_basket_click()
    page.solve_quiz_and_get_code()

    page.success_message_should_dissapear()


@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LINKS[1])
    page.open()
    page.should_be_login_link()


@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINKS[1])
    page.open()
    page.go_to_login_page()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINKS[1])
    page.open()
    page.go_to_basket_page()
    
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_does_not_have_items()
    basket_page.basket_should_be_empty()