from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# 1. Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

for i in range(3):  # Повторить 3 раза
    
    # 2. Найти кнопку по классу 
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    
    # 3. Кликнуть и вывести результат
    print(f"Попытка {i + 1}: Клик на кнопку с текстом '{button.text}'")
    button.click()
    print("Успешно!")
    sleep(1)

driver.quit()

