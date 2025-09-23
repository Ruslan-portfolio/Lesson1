from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, seconds):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(seconds)
    
    def click_number(self, number):
        """Нажимает цифровую кнопку (0-9)"""
        numbers = {
            7: "span.btn.btn-outline-primary:nth-child(1)",
            8: "span.btn.btn-outline-primary:nth-child(2)",
            9: "span.btn.btn-outline-primary:nth-child(3)",
            4: "span.btn.btn-outline-primary:nth-child(5)",
            5: "span.btn.btn-outline-primary:nth-child(6)",
            6: "span.btn.btn-outline-primary:nth-child(7)",
            1: "span.btn.btn-outline-primary:nth-child(9)",
            2: "span.btn.btn-outline-primary:nth-child(10)",
            3: "span.btn.btn-outline-primary:nth-child(11)",
            0: "span.btn.btn-outline-primary:nth-child(13)"
        }
        self._driver.find_element(By.CSS_SELECTOR, numbers[number]).click()
    
    def click_operator(self, operator):
        """Нажимает оператор: +, -, *, /"""
        operators = {
            '+': ".keys .operator:nth-child(4)",
            '-': ".keys .operator:nth-child(8)",
            '*': ".keys .operator:nth-child(12)",
            '/': ".keys .operator:nth-child(16)"
        }
        self._driver.find_element(By.CSS_SELECTOR, operators[operator]).click()
    
    def click_equals(self):
        self._driver.find_element(By.CSS_SELECTOR, ".keys .btn-outline-warning").click()
    
    def wait_for_result(self, expected_result, timeout=45):
        WebDriverWait(self._driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), str(expected_result))
        )
    
    def get_result(self):
        result_element = self._driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text