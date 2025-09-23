
from selenium.webdriver.common.by import By
from time import sleep

class Auth:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://www.saucedemo.com/")

    def auth(self, login, password):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        sleep(2)
    