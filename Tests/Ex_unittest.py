import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class TestAbs(unittest.TestCase):
    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(service=Service('../drivers/chromedriver.exe'))
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder= 'Input your first name']")
        input1.send_keys("Test1")
        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder= 'Input your last name']")
        input2.send_keys("Test2")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder= 'Input your email']")
        input3.send_keys("Test3")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        browser.quit()
        self.assertEqual(expected_text, welcome_text, "Registration failed")

    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(service=Service('../drivers/chromedriver.exe'))
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder= 'Input your first name']")
        input1.send_keys("Test1")
        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder= 'Input your last name']")
        input2.send_keys("Test2")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder= 'Input your email']")
        input3.send_keys("Test3")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        browser.quit()
        self.assertEqual(expected_text, welcome_text, "Registration failed")

if __name__ == "__main__":
    unittest.main()



