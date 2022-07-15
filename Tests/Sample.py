from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import os

try:
    link = ""
    browser = webdriver.Chrome(service=Service('../drivers/chromedriver.exe'))
    browser.get(link)

finally:
    browser.quit()