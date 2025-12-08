import allure
from time import sleep  
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages_form.MainPages import MainPage


@allure.title("Тестирование валидации полей формы")
@allure.description("Тест проверяет цветовую индикацию валидных и невалидных полей формы")
@allure.feature("Валидация формы")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_counter():
    """
    Тест проверяет корректность работы валидации полей формы.
    Валидные поля должны подсвечиваться зеленым, невалидные - красным.
    """

    with allure.step("1. Инициализация браузера и главной страницы"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        main_page = MainPage(browser)

    with allure.step("2. Заполнение всех полей формы данными"):
        main_page.test_complete_form(
            "Иван",
            "Петров",
            "Ленина, 55-3",
            "test@skypro.com",
            "+7985899998787",
            " ",  # Пробел для невалидного ZIP-кода
            "Москва",
            "Россия",
            "QA",
            "SkyPro"
        )
        sleep(2)

    with allure.step("3. Отправка формы на сервер"):
        main_page.submit()
        sleep(3)

    with allure.step("4. Получение цветовой индикации всех полей"):
        colors = main_page.search_color()
        
        if colors:
            allure.attach(f"Получено цветов: {len(colors)}", name="Количество полей",
                         attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("Цвета не получены", name="Ошибка",
                         attachment_type=allure.attachment_type.TEXT)

    with allure.step("5. Проверка зеленых полей (валидные данные)"):
        green_fields = ["#first-name", "#last-name", "#address", "#e-mail", 
                       "#phone", "#city", "#country", "#job-position", "#company"]
        
        for field in green_fields:
            if field in colors:
                assert colors[field] == "rgba(15, 81, 50, 1)", f"Поле {field} должно быть зеленым"

    with allure.step("6. Проверка красного поля (невалидный ZIP-код)"):
        if "#zip-code" in colors:
            assert colors["#zip-code"] == "rgba(132, 32, 41, 1)", "Поле zip-code должно быть красным"

    with allure.step("7. Закрытие браузера"):
        browser.quit()


