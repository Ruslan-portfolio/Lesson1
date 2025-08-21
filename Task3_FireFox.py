from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Создаем драйвер для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_element = driver.find_element(By.CSS_SELECTOR, "button[onclick*=addElement]")

# нажать 5 раз
for _ in range(5):
    add_element.click()
    sleep(0.5)

# ищем размер списка delete
button_delete = driver.find_elements(By.CSS_SELECTOR, "button[onclick*=deleteElement]")

print(len(button_delete))

sleep(5)
driver.quit()