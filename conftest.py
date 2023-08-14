import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.wiki_page import WikiPage

URL = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

logo_image = (By.XPATH, "//img[@class='mw-logo-icon']")


@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    driver = webdriver.Chrome(service=Service())
    driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def open_and_load_wiki_page(driver, wait):
    driver.get(URL)
    wait.until(EC.presence_of_element_located(logo_image))
    yield WikiPage(driver)


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    yield wait
