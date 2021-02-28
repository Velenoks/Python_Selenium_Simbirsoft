import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class AuthGmail:
    """Авторизация на gmail.com."""
    URL = 'https://gmail.com'

    def __init__(self, browser, email, password):
        self.browser = browser
        self.email = email
        self.password = password

    def load(self):
        """Загрузка страницы https://gmail.com."""
        self.browser.get(self.URL)
        time.sleep(3)

    def auth(self):
        """Заполнение полей email и password."""
        try:
            self.browser.find_element_by_xpath(
                '//input[@type="email"]'
            ).send_keys(
                self.email, Keys.ENTER
            )
            time.sleep(2)
            self.browser.find_element_by_xpath(
                '//input[@type="password"]'
            ).send_keys(
                self.password, Keys.ENTER
            )
            time.sleep(5)
        except NoSuchElementException:
            print('Поле email или password не найдено.')

