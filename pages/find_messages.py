from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class SearchGmail:
    def __init__(self, browser, to):
        self.browser = browser
        self.to = to

    def search_email(self):
        try:
            self.browser.find_element_by_class_name(
                "gb_ff"
            ).send_keys(
                'from:'+self.to, Keys.ENTER
            )
        except NoSuchElementException:
            print('Поле (Поиск в почте) не найдено.')
        xpath = f"//span[@email='{self.to}']"
        lens = self.browser.find_elements_by_xpath(xpath)
        return int(len(lens)/2)
