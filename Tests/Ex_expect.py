from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    browser = webdriver.Chrome(service=Service('../drivers/chromedriver.exe'))
    browser.get('http://suninjuly.github.io/explicit_wait2.html')


    text =  WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, 'input_value')
    y = str(math.log(abs(12 * math.sin(int(x.text)))))

    label = browser.find_element(By.ID, 'answer')
    label.send_keys(y)

    button1 = browser.find_element(By.ID, 'solve')
    button1.click()
finally:
    time.sleep(10)
    browser.quit()