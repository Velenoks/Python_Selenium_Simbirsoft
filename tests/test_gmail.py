import time

import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = Chrome('D:\\Python\\Python_Selenium_Simbirsoft\\chromedriver.exe')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# class AuthGmail:
#     URL = 'https://gmail.com'
#
#     def __init__(self, browser):
#         self.browser = browser
#
#     def load(self):
#         self.browser.get(self.URL)
#
#     def auth(self):
#         email_elem = self.browser.find_element_by_id('Email')
#         email_elem.send_keys('pavel.zakharov.test')
#         next_button = self.browser.find_element_by_id('next')
#         next_button.click()
#         time.sleep(2)
#         password_elem = self.browser.find_element_by_id('Passwd')
#         password_elem.send_keys('pav123456zak')
#         signin_button = self.browser.find_element_by_id('signIn')
#         signin_button.click()
#
#
# search_page = AuthGmail(browser)
# search_page.load()
# search_page.auth()


def test_basic_duckduckgo_search(browser):
    URL = 'https://gmail.com'
    browser.get(URL)
    email_elem = browser.find_element_by_xpath('//input[@type="email"]')
    email_elem.send_keys('pavel.zakharov.test', Keys.ENTER)
    time.sleep(2)
    password_elem = browser.find_element_by_xpath('//input[@type="password"]')
    password_elem.send_keys('pav123456zak', Keys.ENTER)
    time.sleep(30)
