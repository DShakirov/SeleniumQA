import os

import requests
from selenium.common import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver import ActionChains

from base import BasePage
from selenium.webdriver.common.by import By
from time import sleep

from logger import logger


class TensorSearchLocators:
    """
    Класс для хранения "локаторов"
    """
    CONTACTS_BUTTON = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor.mb-12")
    MORE_DETAILS_LINK = (By.LINK_TEXT, "Подробнее")
    WORKING_BLOCK = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]')
    HOME_TOWN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
    KAMCHATSKIY_KRAY = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span")
    DOWNLOAD_LINK = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div[10]/ul/li[6]/a")
    SBIS_PLUGIN = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]/div[1]/div/div")
    DOWNLOAD_BUTTON = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a")


class PageTestHelper(BasePage):
    """
    Основной класс для управления Selenium'oм
    """
    def click_on_contacts(self):
        """Переход на вкладку "Контакты" на sbis.ru"""
        contacts_button = self.find_element(TensorSearchLocators.CONTACTS_BUTTON)
        contacts_button.click()
        logger.info('Переход на вкладку "Контакты" на sbis.ru')


    def click_on_tensor_banner(self):
        """Клик по баннеру "Tensor" и переход на tensor.ru"""
        tensor_banner = self.find_element(TensorSearchLocators.TENSOR_BANNER)
        action = ActionChains(self.driver)
        action.move_to_element(tensor_banner).click().perform()
        logger.info('Клик по баннеру "Tensor" и переход на tensor.ru')

    def click_on_more_details_link(self):
        """Клик по ссылке "Подробнее на tensor.ru"""
        # Получаем дескрипторы открытых вкладок
        handles = self.driver.window_handles
        # Переключаемся на вторую вкладку
        self.driver.switch_to.window(handles[1])
        elements = self.driver.find_elements(By.TAG_NAME, "a")
        for element in elements:
            if element.text == "Подробнее" and element.get_attribute("href") == "https://tensor.ru/about":
                self.driver.get("https://tensor.ru/about")
                break
        logger.info('Клик по ссылке "Подробнее на tensor.ru')
        sleep(10)

    def click_on_home_town(self):
        """Клик по кнопке стартового города на sbis.ru/contacts"""
        town_link = self.find_element(TensorSearchLocators.HOME_TOWN)
        town_link.click()
        logger.info('Клик по кнопке стартового города на sbis.ru/contacts')

    def go_to_kamchatsky_kray(self):
        """Переход в Камчатский край на sbis.ru/contacts"""
        kamchayskiy_kray_link = self.find_element(TensorSearchLocators.KAMCHATSKIY_KRAY)
        kamchayskiy_kray_link.click()
        logger.info('Переход в Камчатский край на sbis.ru/contacts')

    def click_download_link(self):
        """Клик по ссылке "Скачать" в футере"""
        download_link = self.find_element(TensorSearchLocators.DOWNLOAD_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", download_link)
        download_link.click()
        logger.info('Клик по ссылке "Скачать" в футере')

    def select_plugin(self):
        """Выбор плагина в меню скачивания"""
        download_link = self.find_element(TensorSearchLocators.SBIS_PLUGIN)
        action = ActionChains(self.driver)
        action.move_to_element(download_link).click().perform()
        logger.info('Выбор плагина в меню скачивания')

    def click_download_exe(self):
        """Клик по кнопке скачивания и сохранение файла"""
        download_link = self.find_element(TensorSearchLocators.DOWNLOAD_BUTTON).get_attribute("href")
        #Сохранение файла в указанную локацию
        file_to_save = "C:/Tensortest/sbisplugin-setup-web.exe"
        response = requests.get(download_link, stream=True)
        with open(file_to_save, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        #Получаем размер скачанного файла
        file_size = os.path.getsize(file_to_save)
        #Переводим размер файла в мегабайты и округляем до двух знаков после запятой
        round_file_size = round((file_size/1048576), 2)
        #Проверка того, что файл скачан полностью
        if file_size == int(response.headers['Content-Length']):
            logger.info("Файл успешно скачан")
            return {
                "file_size":  round_file_size,
                "download_result": "File downloaded successfully."
            }
        else:
            logger.error("Скачивание файла не удалось")
            return {
                "file_size": round_file_size,
                "download_result": "File download was not completed."
            }












