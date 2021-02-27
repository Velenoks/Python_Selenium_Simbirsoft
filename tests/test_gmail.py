import time
import pytest
from selenium.webdriver import Chrome

from pages.auth import AuthGmail
from pages.find_messages import SearchGmail
from pages.send_email import SendEmailGmail


EMAIL = 'pavel.zakharov.test'
PASSWORD = 'pav123456zak'
TO_EMAIL = 'assassins1718@yandex.ru'
TOPIC = 'Тестовое задание. Захаров.'


@pytest.fixture
def browser():
    driver = Chrome('D:\\Python\\Python_Selenium_Simbirsoft\\chromedriver.exe')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_gmail(browser):
    auth_page = AuthGmail(browser, EMAIL, PASSWORD)
    auth_page.load()
    time.sleep(2)
    auth_page.auth()
    time.sleep(2)
    assert EMAIL in browser.title, 'Авторизация не выполнена.'
    find_email = SearchGmail(browser, TO_EMAIL)
    unit = find_email.search_email()
    time.sleep(2)
    send_email_page = SendEmailGmail(browser, TO_EMAIL, TOPIC, unit)
    send_email_page.send_email()
    time.sleep(2)
