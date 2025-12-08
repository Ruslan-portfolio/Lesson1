from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Page Object для веб-калькулятора с задержкой вычислений."""

    def __init__(self, driver):
        """
        Открывает страницу калькулятора.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    @allure.step("Установить задержку вычислений на {seconds} секунд")
    def set_delay(self, seconds):
        """
        Устанавливает время задержки вычислений.
        
        Args:
            seconds: Количество секунд задержки
        """
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(seconds)
    
    @allure.step("Нажать цифровую кнопку: {number}")
    def click_number(self, number):
        """
        Нажимает цифровую кнопку калькулятора.
        
        Args:
            number: Цифра от 0 до 9
        """
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
    
    @allure.step("Нажать оператор: '{operator}'")
    def click_operator(self, operator):
        """
        Нажимает кнопку математического оператора.
        
        Args:
            operator: Математический оператор (+, -, *, /)
        """
        operators = {
            '+': ".keys .operator:nth-child(4)",
            '-': ".keys .operator:nth-child(8)",
            '*': ".keys .operator:nth-child(12)",
            '/': ".keys .operator:nth-child(16)"
        }
        
        self._driver.find_element(By.CSS_SELECTOR, operators[operator]).click()
    
    @allure.step("Нажать кнопку 'равно'")
    def click_equals(self):
        """
        Нажимает кнопку равно для выполнения вычисления.
        """
        self._driver.find_element(By.CSS_SELECTOR, ".keys .btn-outline-warning").click()
    
    @allure.step("Ожидать результат вычислений: ожидается {expected_result}, таймаут {timeout} секунд")
    def wait_for_result(self, expected_result, timeout=45):
        """
        Ожидает появления результата на экране.
        
        Args:
            expected_result: Ожидаемый результат
            timeout: Максимальное время ожидания
        """
        WebDriverWait(self._driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), 
                str(expected_result)
            )
        )
    
    @allure.step("Получить результат вычислений")
    def get_result(self):
        """
        Получает текст результата с экрана калькулятора.
        
        Returns:
            Текст результата вычислений
        """
        result_element = self._driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text