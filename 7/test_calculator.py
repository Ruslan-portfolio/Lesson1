from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Устанавливаем задержку 45 секунд
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    # Нажимаем кнопки: 7 + 8 =
    
    # Кнопка 7 - первая цифровая кнопка
    driver.find_element(By.CSS_SELECTOR, ".keys .btn-outline-primary:nth-child(1)").click()
    
    # Кнопка + - первый оператор (4-й элемент в контейнере)
    driver.find_element(By.CSS_SELECTOR, ".keys .operator:nth-child(4)").click()
    
    # Кнопка 8 - вторая цифровая кнопка
    driver.find_element(By.CSS_SELECTOR, ".keys .btn-outline-primary:nth-child(2)").click()
    
    # Кнопка = 
    driver.find_element(By.CSS_SELECTOR, ".keys .btn-outline-warning").click()
    
    # Ждем результат в течение 45 секунд
    result_element = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    
    # Ждем результат и получаем текст
    result = WebDriverWait(driver, 45).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen"))
    ).text

    # Проверяем результат
    assert result == "15"