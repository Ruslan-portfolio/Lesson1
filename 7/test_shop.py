from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_shopping():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    
    # Авторизация
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    sleep(3)
    
    # Добавление товаров в корзину через CSS селекторы
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    sleep(3)

    # Переход в корзину
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    
    sleep(3)

    # Нажатие Checkout
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    
    sleep(3)

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
    
    sleep(3)

    # Продолжение
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    
    sleep(3)

    # Чтение итоговой стоимости
    total_element = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    total_text = total_element.text
    total_amount = total_text.replace("Total: $", "")
    
    sleep(3)

    # Проверка суммы
    assert total_amount == "58.29"
    
    driver.quit()

