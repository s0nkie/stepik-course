import time
from selenium import webdriver


def test_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    # time.sleep(30)
    button = browser.find_element_by_class_name(
        "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button != None, 'Add to cart button not found'
