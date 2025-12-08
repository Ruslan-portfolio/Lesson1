import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_calculator.CalculatorPage import CalculatorPage


@allure.title("Тестирование калькулятора с задержкой выполнения операций")
@allure.description("Тест проверяет работу веб-калькулятора с установкой задержки вычислений 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    """
    Тест проверяет работу калькулятора с задержкой вычислений.
    Проводится операция 7 + 8 и проверяется результат.
    """
    
    with allure.step("1. Инициализация браузера и переход на страницу калькулятора"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        calculator_page = CalculatorPage(driver)

    with allure.step("2. Установка времени задержки вычислений"):
        calculator_page.set_delay("5")

    with allure.step("3. Выполнение математической операции 7 + 8"):
        calculator_page.click_number(7)
        calculator_page.click_operator('+')
        calculator_page.click_number(8)
        calculator_page.click_equals()

    with allure.step("4. Ожидание результата с учетом задержки"):
        calculator_page.wait_for_result(15, 50)

    with allure.step("5. Проверка корректности результата вычислений"):
        result = calculator_page.get_result()
        assert result == "15", f"Ожидался результат 15, получен {result}"

    with allure.step("6. Закрытие браузера"):
        driver.quit()