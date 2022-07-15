from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome(service=Service('../drivers/chromedriver.exe'))
    browser.get("http://suninjuly.github.io/selects1.html")
    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    y = int(num1.text) + int(num2.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(y))
    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()