import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CUSTOM_CHROME = False
PATH_TO_CHROME = r'/Users/kinteriq/drivers/chromedriver'


def pytest_addoption(parser):
    parser.addoption('--language', action='store',
        default='en', help='Choose language.')


@pytest.fixture(scope='function')
def browser(request):
    lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': lang
    })
    if CUSTOM_CHROME:
        browser = webdriver.Chrome(PATH_TO_CHROME, options=options)
    else:
        browser = webdriver.Chrome(options=options)
    print(f'\nStart browser: language={lang}.')
    yield browser
    print(f'\nQuit browser; language={lang}.')
    browser.quit()