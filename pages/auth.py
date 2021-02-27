import time

from selenium.webdriver.common.keys import Keys


class AuthGmail:
    URL = 'https://gmail.com'

    def __init__(self, browser, email, password):
        self.browser = browser
        self.email = email
        self.password = password

    def load(self):
        self.browser.get(self.URL)

    def auth(self):
        email_elem = self.browser.find_element_by_xpath(
            '//input[@type="email"]')
        email_elem.send_keys(self.email, Keys.ENTER)
        time.sleep(2)
        password_elem = self.browser.find_element_by_xpath(
            '//input[@type="password"]')
        password_elem.send_keys(self.password, Keys.ENTER)
