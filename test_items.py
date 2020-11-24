import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_add_button(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
           f'-work_207/'
    browser.get(link)
    time.sleep(30)
    add_cart_button = WebDriverWait(browser,10).until\
        (
            expected_conditions.presence_of_element_located(
                (
                    By.CSS_SELECTOR, 'button.btn-add-to-basket'
                )
            )
        )

    assert add_cart_button, 'Expected that button exists but it is not'