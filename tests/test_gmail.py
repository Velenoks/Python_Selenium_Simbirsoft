import os
import time

from pages.auth import AuthGmail
from pages.find_messages import SearchGmail
from pages.send_email import SendEmailGmail


EMAIL = os.environ.get("EMAIL", 'pavel.zakharov.test@gmail.com')
PASSWORD = os.environ.get("PASSWORD", 'pav123456zak')
TO_EMAIL = os.environ.get("TO_EMAIL", 'assassins1718@yandex.ru')
TOPIC = 'Тестовое задание. Захаров.'


def test_gmail(selenium):
    auth_page = AuthGmail(selenium, EMAIL, PASSWORD)
    auth_page.load()
    time.sleep(3)
    auth_page.auth()
    time.sleep(3)
    assert EMAIL in selenium.title, 'Авторизация не выполнена.'
    find_email = SearchGmail(selenium, TO_EMAIL)
    unit = find_email.search_email()
    time.sleep(3)
    send_email_page = SendEmailGmail(selenium, TO_EMAIL, TOPIC, unit)
    send_email_page.send_email()
    time.sleep(3)
