from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """Page Object для страницы формы с валидацией."""

    def __init__(self, driver):
        """
        Открывает страницу формы для заполнения.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнить форму данными")
    def test_complete_form(self, first_name, last_name, address, e_mail, phone, zip_code, city, country, job_position, company):
        """
        Заполняет все поля формы данными.
        
        Args:
            first_name: Имя
            last_name: Фамилия
            address: Адрес
            e_mail: Email
            phone: Телефон
            zip_code: ZIP код
            city: Город
            country: Страна
            job_position: Должность
            company: Компания
        """
        first_name_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='first-name']")))
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='last-name']")))
        last_name_field.send_keys(last_name)
        
        address_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='address']")))
        address_field.send_keys(address)

        e_mail_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='e-mail']")))
        e_mail_field.send_keys(e_mail)

        phone_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='phone']")))
        phone_field.send_keys(phone)

        zip_code_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='zip-code']")))
        zip_code_field.send_keys(zip_code)

        city_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='city']")))
        city_field.send_keys(city)

        country_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='country']")))
        country_field.send_keys(country)

        job_position_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='job-position']")))
        job_position_field.send_keys(job_position)

        company_field = WebDriverWait(self._driver, 15).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='company']")))
        company_field.send_keys(company)

    @allure.step("Отправить форму")
    def submit(self):
        """
        Нажимает кнопку отправки формы.
        """
        button = WebDriverWait(self._driver, 15).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
        button.click()
    
    @allure.step("Получить цвета полей формы")
    def search_color(self):
        """
        Возвращает словарь с цветами всех полей формы.
        
        Returns:
            Словарь где ключ - селектор поля, значение - цвет
        """
        green_fields = [
            "#first-name", "#last-name", "#address", "#e-mail", 
            "#phone", "#city", "#country", "#job-position", "#company"
        ]
    
        colors = {}
    
        for field in green_fields:
            element = WebDriverWait(self._driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, field)))
            colors[field] = element.value_of_css_property("color")

        zip_code_element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#zip-code")))
        colors["#zip-code"] = zip_code_element.value_of_css_property("color")
    
        return colors
        