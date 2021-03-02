from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class AuthLocators:
    """Локаторы для авторизации."""
    LOCATOR_EMAIL_FIELD = (By.XPATH, '//input[@type="email"]')
    LOCATOR_NEXT_BUTTON = (By.ID, 'identifierNext')
    LOCATOR_PASSWORD_FIELD = (By.NAME, 'password')


class AuthHelper(BasePage):
    """Авторизация на Gmail."""

    def enter_email(self, word):
        """Ввод email."""
        email_field = self.find_element(AuthLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(word, Keys.ENTER)
        return email_field

    def enter_password(self, word):
        """Ввод пароля."""
        password_field = self.find_element(AuthLocators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(word, Keys.ENTER)
        return password_field
