from time import sleep  
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_form.MainPages import MainPage

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.test_complete_form("Иван", 
                                  "Петров", 
                                  "Ленина, 55-3", 
                                  "test@skypro.com", 
                                  "+7985899998787", 
                                  " ",
                                  "Москва",
                                  "Россия",
                                  "QA", 
                                  "SkyPro")
    sleep(2)
    
    main_page.submit()
    sleep(2)

    # Получаем цвета всех полей
    colors = main_page.search_color()
    
    # Проверяем зеленые поля
    green_fields = ["#first-name", "#last-name", "#address", "#e-mail", 
                   "#phone", "#city", "#country", "#job-position", "#company"]
    
    for field in green_fields:
        assert colors[field] == "rgba(15, 81, 50, 1)", f"Поле {field} должно быть зеленым"
    
    # Проверяем красное поле
    assert colors["#zip-code"] == "rgba(132, 32, 41, 1)", "Поле zip-code должно быть красным"

    browser.quit()


