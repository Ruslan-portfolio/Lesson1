from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_calculator.CalculatorPage import CalculatorPage

def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calculator_page = CalculatorPage(driver)
    calculator_page.set_delay("45")
    
    calculator_page.click_number(7)   
    calculator_page.click_operator('+')
    calculator_page.click_number(8)    
    calculator_page.click_equals()
    calculator_page.wait_for_result(15, 45)
    
    result = calculator_page.get_result()
    assert result == "15"
    
    driver.quit()