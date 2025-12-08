from selenium.webdriver.common.by import By
import allure


class MainPage:
    """Page Object для главной страницы магазина."""

    def __init__(self, driver):
        """
        Инициализирует главную страницу магазина.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self._driver = driver

    @allure.step("Добавить товары в корзину")
    def add_products(self):
        """
        Добавляет три товара в корзину.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Перейти в корзину")
    def go_to_the_cart(self):
        """
        Переходит в корзину покупок.
        """
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
