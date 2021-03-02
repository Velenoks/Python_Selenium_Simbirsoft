import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


load_dotenv()
TO_EMAIL = os.getenv('TO_EMAIL')


class FindLocators:
    """Локаторы для поиска."""
    LOCATOR_SEARCH_FIELD = (By.XPATH, '//input[@aria-label="Поиск в почте"]')
    LOCATOR_COUNT_EMAIL = (By.XPATH, f'//span[@email="{TO_EMAIL}"]')


class FindHelper(BasePage):
    """Поиск и подсчет писем."""

    def search_email(self, word):
        """Поиск писем."""
        search_email = self.find_element(FindLocators.LOCATOR_SEARCH_FIELD)
        search_email.send_keys('from:'+word, Keys.ENTER)
        return search_email

    def count_emails(self):
        """Подсчет писем."""
        count_emails = self.find_elements(FindLocators.LOCATOR_COUNT_EMAIL)
        lens = len(count_emails) / 2
        return int(lens)
