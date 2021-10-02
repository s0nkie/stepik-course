import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    languages = ['es', 'en', 'ru', 'fr']
    if user_language in languages:
        print('\nBrowser start with choosen language')
    else:
        raise pytest.UsageError('Choose the language')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(25.0)
    yield browser
    browser.quit()
