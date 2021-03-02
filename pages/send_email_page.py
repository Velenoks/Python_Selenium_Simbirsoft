import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class SendLocators:
    """Локаторы для создания и отправки email."""
    LOCATOR_WRITE_BUTTON = (By.XPATH, '//div[text()="Написать"]')
    LOCATOR_TO_EMAIL = (By.NAME, 'to')
    LOCATOR_SUBJECTBOX_EMAIL = (By.NAME, 'subjectbox')
    LOCATOR_TEXT_EMAIL = (By.CSS_SELECTOR, 'div[aria-label="Тело письма"]')


class SendHelper(BasePage):
    """Создание и отправка email."""
    def write_button(self):
        """Нажать кнопку 'Написать'."""
        button = self.find_element(SendLocators.LOCATOR_WRITE_BUTTON)
        button.click()

    def write_email(self, to_email, topic, unit):
        """Создание и отправка email."""
        email_to = self.find_element(SendLocators.LOCATOR_TO_EMAIL)
        email_to.send_keys(to_email)
        topic_email = self.find_element(SendLocators.LOCATOR_SUBJECTBOX_EMAIL)
        topic_email.send_keys(topic)
        text = self.text_for_email(unit)
        text_email = self.find_element(SendLocators.LOCATOR_TEXT_EMAIL)
        text_email.send_keys(text, Keys.CONTROL, Keys.ENTER)
        time.sleep(3)

    def text_for_email(self, unit):
        """Выбор нужного окончания."""
        text = f'Всего было найдено {unit} '
        if 10 < unit < 15:
            text += 'сообщений'
        elif unit % 10 == 1:
            text += 'сообщение'
        elif 1 < unit % 10 < 5:
            text += 'сообщения'
        elif 0 == unit % 10 or unit % 10 > 4:
            text += 'сообщений'
        return text
