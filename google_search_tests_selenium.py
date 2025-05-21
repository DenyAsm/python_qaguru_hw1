from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_captcha_should_be_shown():
    driver = webdriver.Chrome()
    driver.get('https://google.com')

    search_input = driver.find_element(By.NAME, 'q')
    search_input.send_keys('qa.guru')
    search_input.send_keys(Keys.RETURN)

    time.sleep(1)  # Подождать загрузку страницы (лучше заменить на WebDriverWait)

    assert 'Об этой странице' in driver.page_source
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_captcha_should_be_shown1():
    driver = webdriver.Chrome()
    driver.get('https://google.com')

    search_input = driver.find_element(By.NAME, 'q')
    search_input.send_keys('qa.guru')
    search_input.send_keys(Keys.RETURN)

    # Replace time.sleep with WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Об этой странице')]")))

    assert 'Об этой странице' in driver.page_source
    driver.quit()