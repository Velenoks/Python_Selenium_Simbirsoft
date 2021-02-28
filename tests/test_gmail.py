import os
import pytest
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

from pages.auth import AuthGmail
from pages.find_messages import SearchGmail
from pages.send_email import SendEmailGmail


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
    def test_gmail(self, selenium):
        """Авторизация на gmail.com, поиск сообщений и отправка сообщения."""
        auth_page = AuthGmail(selenium, EMAIL, PASSWORD)
        auth_page.load()
        with allure.step('Делаем скриншот авторизации'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_auth',
                          attachment_type=AttachmentType.PNG)
        assert selenium.title == 'Gmail', 'Страница gmail.com не загрузилась.'
        auth_page.auth()
        with allure.step('Делаем скриншот главной страницы'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_main_gmail',
                          attachment_type=AttachmentType.PNG)
        assert EMAIL in selenium.title, 'Авторизация не выполнена.'
        find_email = SearchGmail(selenium, TO_EMAIL)
        unit = find_email.search_email()
        with allure.step('Делаем скриншот найденых сообщений'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_sind_messages',
                          attachment_type=AttachmentType.PNG)
        assert isinstance(unit, int), 'Поиск сообщений не выполнен.'
        send_email_page = SendEmailGmail(selenium, TO_EMAIL, TOPIC, unit)
        send_email_page.send_email()
        with allure.step('Делаем скриншот отправленных сообщений'):
            allure.attach(selenium.get_screenshot_as_png(),
                          name='screenshot_sind_messages',
                          attachment_type=AttachmentType.PNG)
