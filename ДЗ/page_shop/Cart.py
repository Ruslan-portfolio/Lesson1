from selenium.webdriver.common.by import By

class Cart:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/cart.html")

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()