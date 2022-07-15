from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math

try:
    browser = webdriver.Chrome(service=Service('../drivers/chromedriver.exe'))
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    alert = browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, 'input_value')
    y = str(math.log(abs(12 * math.sin(int(x.text)))))

    label = browser.find_element(By.ID, 'answer')
    label.send_keys(y)

    button1 = browser.find_element(By.CLASS_NAME, 'btn')
    button1.click()

finally:
    time.sleep(10)
    browser.quit()