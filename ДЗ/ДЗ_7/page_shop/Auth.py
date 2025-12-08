from selenium.webdriver.common.by import By
from time import sleep
import allure


class Auth:
    """Page Object для страницы авторизации."""

    def __init__(self, driver):
        """
        Открывает страницу авторизации.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести логин и пароль")
    def auth(self, login, password):
        """
        Вводит логин и пароль в форму авторизации.
        
        Args:
            login: Имя пользователя
            password: Пароль пользователя
        """
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    @allure.step("Нажать кнопку входа")
    def submit(self):
        """
        Нажимает кнопку входа в систему.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        sleep(2)