from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class SendEmailGmail:
    def __init__(self, browser, to, topic, unit):
        self.browser = browser
        self.to = to
        self.topic = topic
        self.unit = unit

    def send_email(self):
        try:
            self.browser.find_element_by_xpath(
                "//div[text()='Написать']"
            ).click()
        except NoSuchElementException:
            print('Кнопка (Написать) не найдена')
        email_to = self.browser.find_element_by_name("to")
        email_to.send_keys(self.to)
        topic_email = self.browser.find_element_by_name("subjectbox")
        topic_email.send_keys(self.topic)
        text = self.text_for_email()
        text_email = self.browser.find_element_by_css_selector(
            "div[aria-label='Тело письма']")
        text_email.send_keys(text, Keys.CONTROL, Keys.ENTER)

    def text_for_email(self):
        text = f'Всего было найдено {self.unit} '
        if 10 < self.unit < 15:
            text += 'сообщений'
        elif self.unit % 10 == 1:
            text += 'сообщение'
        elif 1 < self.unit % 10 < 5:
            text += 'сообщения'
        elif 0 == self.unit % 10 or self.unit % 10 > 4:
            text += 'сообщений'
        return text
