import time
import pytest

from selenium.webdriver import Chrome

from pages.auth import AuthGmail
from pages.send_email import SendEmailGmail


@pytest.fixture
def browser():
    driver = Chrome('D:\\Python\\Python_Selenium_Simbirsoft\\chromedriver.exe')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_basic_duckduckgo_search(browser):
    email = 'pavel.zakharov.test'
    password = 'pav123456zak'
    auth_page = AuthGmail(browser, email, password)
    auth_page.load()
    time.sleep(2)
    auth_page.auth()
    time.sleep(3)
    send_email_page = SendEmailGmail(browser)
    send_email_page.send_email()
