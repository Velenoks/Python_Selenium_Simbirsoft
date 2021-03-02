import os
import pytest
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

from pages.auth_page import AuthHelper
from pages.find_messages_page import FindHelper
from pages.send_email_page import SendHelper

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')
TOPIC = 'Тестовое задание. Захаров.'


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.set_page_load_timeout(10)
    return selenium


class TestGmail:

    @allure.feature('Тест серсива GMail.')
    @allure.story('Авторизация на gmail.com, '
                  'поиск сообщений и отправка сообщения.')
    @allure.severity('blocker')
    def test_auth(self, selenium):
        """Авторизация на gmail.com, поиск сообщений и отправка сообщения."""
        gmail_page = AuthHelper(selenium)
        gmail_page.go_to_site()
        with allure.step('Делаем скриншот авторизации'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_auth',
                          attachment_type=AttachmentType.PNG)
        assert selenium.title == 'Gmail', 'Страница gmail.com не загрузилась.'
        gmail_page.enter_email(EMAIL)
        gmail_page.enter_password(PASSWORD)
        gmail_page = FindHelper(selenium)
        with allure.step('Делаем скриншот главной страницы'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_main_gmail',
                          attachment_type=AttachmentType.PNG)
        assert EMAIL in gmail_page.title(), 'Авторизация не выполнена.'
        gmail_page.search_email(TO_EMAIL)
        emails = gmail_page.count_emails()
        with allure.step('Делаем скриншот найденых сообщений'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_sind_messages',
                          attachment_type=AttachmentType.PNG)
        assert isinstance(emails, int), 'Поиск сообщений не выполнен.'
        gmail_page = SendHelper(selenium)
        gmail_page.write_button()
        gmail_page.write_email(TO_EMAIL, TOPIC, emails)
        with allure.step('Делаем скриншот отправленных сообщений'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_sind_messages',
                          attachment_type=AttachmentType.PNG)
