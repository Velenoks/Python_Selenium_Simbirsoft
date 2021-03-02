from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Методы для работы с webdriver."""

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://gmail.com'

    def find_element(self, locator, time=10):
        """Найти элемент."""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не могу найти элемент {locator}.")

    def find_elements(self, locator, time=10):
        """Найти элементы."""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не могу найти элементы {locator}.")

    def go_to_site(self):
        """Загрузить страницу."""
        return self.driver.get(self.base_url)

    def title(self):
        """Получить заголовок."""
        url = self.driver.current_url
        WebDriverWait(self.driver, 10).until(EC.url_changes(url))
        return self.driver.title
