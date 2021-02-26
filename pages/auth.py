import time
from selenium.webdriver.common.by import By


class AuthGmail:
    URL = 'https://gmail.com'
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def auth(self):
        email_elem = self.browser.find_element_by_id('Email')
        email_elem.send_keys('pavel.zakharov.test')
        next_button = self.browser.find_element_by_id('next')
        next_button.click()
        time.sleep(2)
        password_elem = self.browser.find_element_by_id('Passwd')
        password_elem.send_keys('pav123456zak')
        signin_button = self.browser.find_element_by_id('signIn')
        signin_button.click()
