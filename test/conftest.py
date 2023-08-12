import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def driver():
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(), options=options)
    yield driver
    driver.quit()
