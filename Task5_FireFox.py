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
driver.get("http://uitestingplayground.com/classattr")

# 2. Поиск кнопки
blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))

# 3. Клик по кнопке
print(f"Кликаем на кнопку с текстом '{blue_button.text}'")
blue_button.click()
print("Успешно")

sleep(5)

driver.quit()