import time

from selenium.webdriver.common.keys import Keys


class SendEmailGmail:
    def __init__(self, browser):
        self.browser = browser

    def send_email(self):
        self.browser.find_element_by_xpath("//div[text()='Написать']").click()
        email_to = self.browser.find_element_by_name("to")
        email_to.send_keys('pavel.zakharov.1994@yandex.ru')
        time.sleep(2)
        team_email = self.browser.find_element_by_name("subjectbox")
        team_email.send_keys("Тестовое задание. Захаров")
        time.sleep(2)
        text_email = self.browser.find_element_by_css_selector(
            "div[aria-label='Тело письма']")
        text_email.send_keys("Было найдено n письма")
        time.sleep(2)
        text_email.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(4)
