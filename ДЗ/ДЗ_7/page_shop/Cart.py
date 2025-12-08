from selenium.webdriver.common.by import By
import allure


class Cart:
    """Page Object для страницы корзины."""

    def __init__(self, driver):
        """
        Открывает страницу корзины.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Начать оформление заказа")
    def submit(self):
        """
        Нажимает кнопку оформления заказа.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()