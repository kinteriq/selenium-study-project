import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
    browser = webdriver.Chrome(PATH_TO_CHROME, options=options)
    print(f'Start browser: language={lang}.')
    yield browser
    print(f'Quit browser; language={lang}.')
    browser.quit()