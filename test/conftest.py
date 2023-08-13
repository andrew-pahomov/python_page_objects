import allure
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@allure.step('Открытие страницы в браузере')
@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service(), options=options)
    yield driver
    driver.quit()

