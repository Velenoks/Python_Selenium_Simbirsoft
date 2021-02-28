import os
import pytest
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


class Test01Gmail:

    def test_gmail(self, selenium):
        """Авторизация на gmail.com, поиск сообщений и отправка сообщения."""
        auth_page = AuthGmail(selenium, EMAIL, PASSWORD)
        auth_page.load()
        auth_page.auth()
        assert EMAIL in selenium.title, 'Авторизация не выполнена.'
        find_email = SearchGmail(selenium, TO_EMAIL)
        unit = find_email.search_email()
        assert isinstance(unit, int), 'Поиск сообщений не выполнен.'
        send_email_page = SendEmailGmail(selenium, TO_EMAIL, TOPIC, unit)
        send_email_page.send_email()
