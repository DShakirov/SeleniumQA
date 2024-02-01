from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс, от него наследуется класс для управления Selenium
    """
    def __init__(self, driver):
        """
        Определяем драйвер Selenium и стартовую страницу
        """
        self.driver = driver
        self.base_url = "https://sbis.ru"

    def find_element(self, locator, time=120):
        """Находим один элемент на странице"""
        WebDriverWait(self.driver, time).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete',
            "Page was not fully loaded"
        )
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Element {locator} is not visible"
        )
        WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div.preload-overlay')),
            message="Preload overlay is still visible"
        )
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} is not clickable"
        )

    def find_elements(self, locator, time=60):
        """Находим на странице все элементы, удовлетворяющие условиям"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        """Переходим на главную странице"""
        return self.driver.get(self.base_url)
