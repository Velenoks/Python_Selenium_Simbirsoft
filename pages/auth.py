import time

from selenium.common.exceptions import NoSuchElementException
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
        try:
            self.browser.find_element_by_xpath(
                '//input[@type="email"]'
            ).send_keys(
                self.email, Keys.ENTER
            )
            time.sleep(3)
            self.browser.find_element_by_xpath(
                '//input[@type="password"]'
            ).send_keys(
                self.password, Keys.ENTER
            )
        except NoSuchElementException:
            print('Поле email или password не найдено.')

