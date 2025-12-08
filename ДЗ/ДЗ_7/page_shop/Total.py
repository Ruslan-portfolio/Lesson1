from selenium.webdriver.common.by import By
import allure


class Total:
    """Page Object для страницы итоговой суммы."""

    def __init__(self, driver):
        """
        Открывает страницу итоговой суммы.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")

    @allure.step("Получить итоговую сумму")
    def total(self):
        """
        Получает итоговую сумму заказа.
        
        Returns:
            Итоговая сумма заказа
        """
        total_element = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")
        return total_amount