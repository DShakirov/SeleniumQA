import re

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By


def compare_images_size(browser):

    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    photos = [
        browser.find_element(By.XPATH,
                             '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div['
                             '2]/div[1]/a/div[1]/img'),
        browser.find_element(By.XPATH,
                             '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div['
                             '2]/div[2]/a/div[1]/img'),
        browser.find_element(By.XPATH,
                             '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div['
                             '2]/div[3]/a/div[1]/img'),
        browser.find_element(By.XPATH,
                             '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div['
                             '2]/div[4]/a/div[1]/img'),
    ]
    result = True
    width = photos[0].get_attribute("width")
    height = photos[0].get_attribute("height")
    # Тест не пройдет, если ширина или высота любой из фотографий отличается от первой
    for photo in photos[1:]:
        if photo.get_attribute("width") != width or photo.get_attribute("height") != height:
            result = False
            break
    return result

def get_present_town(browser):
    try:
        element = browser.find_element(By.XPATH,
                                      "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
        text = element.text
        return text
    except:
        return None

def partners_list_exists(browser):
    try:
        element = browser.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[3]/div/div[2]/div[2]/div")
        return True
    except NoSuchElementException:
        return False

def kamchatsky_kray_exists(browser):
    try:
        element = browser.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span")
        return True
    except NoSuchElementException:
        return False

def get_partners(browser):
    try:
        element = browser.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]")
        text = element.text
        return text
    except NoSuchElementException:
        return None

def find_block(browser):

    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    elements = browser.find_elements(By.TAG_NAME, "div")
    for element in elements:
        try:
            if "Сила в людях" in element.text:
                return True
        except StaleElementReferenceException as e:
            continue
    return False

def get_download_size(browser):
    element = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a")
    text = element.text
    file_size = float(re.search(r'\d\.\d{2}', text).group())
    return file_size





