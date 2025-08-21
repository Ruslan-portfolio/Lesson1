from time import  sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("http://the-internet.herokuapp.com/login")

# найти поля логин, пароль
Username = driver.find_element(By.CSS_SELECTOR, "#username")
Username.send_keys("tomsmith")
sleep(2)
Password = driver.find_element(By.CSS_SELECTOR, "#password")
Password.send_keys("SuperSecretPassword!")
sleep(2)

# жмакаем кнопку
Button = driver.find_element(By.CSS_SELECTOR, ".radius")
Button.click()
sleep(5)

driver.quit()

