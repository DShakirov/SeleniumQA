from page import PageTestHelper
from time import sleep
from utils import (
    find_block,
    compare_images_size,
    get_present_town,
    partners_list_exists,
    kamchatsky_kray_exists,
    get_partners,
    get_download_size
)


class TestFirstScenario:
    """
        1) Перейти на https://sbis.ru/ в раздел "Контакты"
        2) Найти баннер Тензор, кликнуть по нему
        3) Перейти на https://tensor.ru/
        4) Проверить, что есть блок "Сила в людях"
        5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
        https://tensor.ru/about
        6) Находим раздел "Работаем" и проверяем, что у всех фотографий
        хронологии одинаковые высота (height) и ширина (width)
    """
    def test_first_part(self, browser):
        main_page = PageTestHelper(browser)
        # Открываем "http://sbis.ru"
        main_page.go_to_site()
        # "Кликаем по кнопке "Контакты""
        main_page.click_on_contacts()
        # "Кликаем по баннеру "Tensor""
        main_page.click_on_tensor_banner()
        sleep(30)
        #Проверяем наличие блока "Сила в людях"
        block = find_block(browser)
        assert block == True
        # Клик на ссылку "Подробнее"#
        sleep(15)
        main_page.click_on_more_details_link()
        # Проверяем на какую страницу мы попали
        current_url = browser.current_url
        assert current_url == "https://tensor.ru/about"
        # Находим блок "Работаем" и проверяем фотографии на одинаковый размер
        assert compare_images_size(browser) == True


class TestSecondScenario:
    """
    1) Перейти на https://sbis.ru/ в раздел "Контакты"
    2) Проверить, что определился ваш регион (в нашем примере
    Ярославская обл.) и есть список партнеров.
    3) Изменить регион на Камчатский край
    4) Проверить, что подставился выбранный регион, список партнеров
    изменился, url и title содержат информацию выбранного региона
    """

    def test_second_part(self, browser):
        main_page = PageTestHelper(browser)
        #Открываем "http://sbis.ru"
        main_page.go_to_site()
        sleep(10)
        # "Кликаем по кнопке "Контакты"
        main_page.click_on_contacts()
        # Проверяем текущий город
        text = get_present_town(browser)
        assert text == "г. Севастополь"
        # проверяем список партнеров
        assert partners_list_exists(browser) == True
        main_page.click_on_home_town()
        sleep(10)
        # Проверяем что Камчатский край присутствует в доступных локациях
        assert kamchatsky_kray_exists(browser) == True
        # Переходим в Камчатский край
        main_page.go_to_kamchatsky_kray()
        # Проверяем адресную строку браузера
        current_url = browser.current_url
        assert current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
        # Проверяем текущий город
        text = get_present_town(browser)
        assert text == "Камчатский край"
        partners = get_partners(browser)
        assert partners == "СБИС - Камчатка"


class TestThirdScenario:
    """
    1) Перейти на https://sbis.ru/
    2) В Footer'e найти и перейти "Скачать СБИС"
    3) Скачать СБИС Плагин для вашей для windows, веб-установщик в
    папку с данным тестом
    4) Убедиться, что плагин скачался
    5) Сравнить размер скачанного файла в мегабайтах. Он должен
    совпадать с указанным на сайте (в примере 3.64 МБ).
    """
    def test_third_part(self, browser):
        main_page = PageTestHelper(browser)
        #Открываем "http://sbis.ru"
        main_page.go_to_site()
        sleep(40)
        #Переходим в footer, кликаем на "Скачать СБИС"
        main_page.click_download_link()
        sleep(20)
        #Выбираем "плагин"
        main_page.select_plugin()
        current_url = browser.current_url
        assert current_url == "https://sbis.ru/download?tab=plugin&innerTab=default"
        sleep(20)
        #Скачиваем файл
        download = main_page.click_download_exe()
        download_result = download["download_result"]
        file_size = download["file_size"]
        sleep(30)
        assert download_result == "File downloaded successfully."
        #Сравниваем размер файла с указанным на сайте
        size_from_page = get_download_size(browser)
        assert file_size == size_from_page

