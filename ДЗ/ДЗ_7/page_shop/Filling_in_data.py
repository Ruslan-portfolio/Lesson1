from selenium.webdriver.common.by import By
import allure


class Data:
    """Page Object для страницы ввода данных доставки."""

    def __init__(self, driver):
        """
        Открывает страницу ввода данных доставки.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    @allure.step("Заполнить данные доставки")
    def filling_in_data(self, first_name, last_name, zip_code):
        """
        Заполняет форму данными для доставки.
        
        Args:
            first_name: Имя получателя
            last_name: Фамилия получателя
            zip_code: Почтовый индекс
        """
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip_code)

    @allure.step("Продолжить оформление")
    def submit(self):
        """
        Нажимает кнопку продолжения оформления.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()