from selenium.webdriver.common.by import By

class Total:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def total(self):
        total_element = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")
        return total_amount
