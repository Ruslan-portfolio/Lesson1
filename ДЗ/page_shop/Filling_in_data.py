from selenium.webdriver.common.by import By

class Data:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def filling_in_data(self, first_name, last_name, zip):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()