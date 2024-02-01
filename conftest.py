import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(executable_path="C:/Tensortest/geckodriver")
    yield driver
    driver.quit()