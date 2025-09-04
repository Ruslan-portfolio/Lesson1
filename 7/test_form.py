from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=first-name]")))
    first_name.send_keys("Иван")

    last_name = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=last-name]")))
    last_name.send_keys("Петров")

    address = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=address]")))
    address.send_keys("Ленина, 55-3")

    e_mail = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=e-mail]")))
    e_mail.send_keys("test@skypro.com")

    phone = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=phone]")))
    phone.send_keys("+7985899998787")

    zip_code = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=zip-code]")))

    city = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=city]")))
    city.send_keys("Москва")

    country = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=country]")))
    country.send_keys("Россия")

    job_position = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=job-position]")))
    job_position.send_keys("QA")

    company = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=company]")))
    company.send_keys("SkyPro")

    sleep(2)

    button = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button"))).click()

    sleep(2)

    # Проверка цветов заполненных полей (зеленый)
    green_fields = [
        "#first-name", "#last-name", "#address", "#e-mail", 
        "#phone", "#city", "#country", "#job-position", "#company"
    ]
    
    for field in green_fields:
        element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, field)))
        actual_color = element.value_of_css_property("color")
        assert actual_color == "rgba(15, 81, 50, 1)", f"Поле {field} должно быть зеленым"

    # Проверка цвета пустого поля (красный)
    zip_code_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#zip-code")))
    actual_color = zip_code_element.value_of_css_property("color")
    assert actual_color == "rgba(132, 32, 41, 1)", "Поле zip-code должно быть красным"

    driver.quit()

