from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math

try:
    browser = webdriver.Chrome(service=Service('../drivers/chromedriver.exe'))
    browser.get('http://suninjuly.github.io/execute_script.html')

    input = browser.find_element(By.ID, 'input_value')
    y = str(math.log(abs(12*math.sin(int(input.text)))))

    label = browser.find_element(By.CLASS_NAME, 'form-control')
    label.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    button.click()
finally:
    time.sleep(5)
    browser.quit()