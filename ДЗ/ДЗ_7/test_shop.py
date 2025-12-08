import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page_shop.Auth import Auth
from page_shop.MainPage import MainPage
from page_shop.Cart import Cart
from page_shop.Filling_in_data import Data
from page_shop.Total import Total

@allure.title("Полный цикл покупки товаров в интернет-магазине")
@allure.description("Тест автоматизирует полный процесс покупки: авторизация, выбор товаров, оформление заказа")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping():
    """
    Интеграционный тест, проверяющий полный процесс покупки товаров.
    Включает все этапы от авторизации до подтверждения заказа.
    """

    with allure.step("1. Запуск браузера и инициализация страниц"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        allure.attach("Браузер Chrome успешно запущен", name="Инициализация", 
                     attachment_type=allure.attachment_type.TEXT)

    with allure.step("2. Авторизация пользователя в системе"):
        auth_page = Auth(browser)
        auth_page.auth("standard_user", "secret_sauce")
        sleep(1)
        auth_page.submit()
        allure.attach("Пользователь: standard_user", name="Учетные данные", 
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach(browser.get_screenshot_as_png(), name="Страница авторизации",
                     attachment_type=allure.attachment_type.PNG)

    with allure.step("3. Добавление товаров в корзину на главной странице"):
        main_page = MainPage(browser)
        main_page.add_products()
        main_page.go_to_the_cart()
        allure.attach("Добавлены товары: рюкзак, футболка, комбинезон", name="Товары в корзине",
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach(browser.get_screenshot_as_png(), name="Товары добавлены",
                     attachment_type=allure.attachment_type.PNG)

    with allure.step("4. Переход к оформлению заказа в корзине"):
        cart_page = Cart(browser)
        cart_page.submit()
        allure.attach("Переход на страницу оформления заказа", name="Корзина",
                     attachment_type=allure.attachment_type.TEXT)

    with allure.step("5. Заполнение данных для доставки"):
        data_page = Data(browser)
        data_page.filling_in_data("Иван", "Петров", "123456")
        data_page.submit()
        allure.attach("Имя: Иван, Фамилия: Петров, ZIP: 123456", name="Данные доставки", 
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach(browser.get_screenshot_as_png(), name="Данные доставки заполнены",
                     attachment_type=allure.attachment_type.PNG)

    with allure.step("6. Проверка итоговой суммы заказа"):
        total_page = Total(browser)
        as_is = total_page.total()
        
        allure.attach(f"Фактическая сумма: {as_is}", name="Итоговая сумма", 
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach("Ожидаемая сумма: 58.29", name="Ожидаемая сумма", 
                     attachment_type=allure.attachment_type.TEXT)
        
        # Скриншот итоговой страницы
        allure.attach(browser.get_screenshot_as_png(), name="Итоговая страница",
                     attachment_type=allure.attachment_type.PNG)
        
        if as_is:
            assert as_is == "58.29", f"Ожидаемая сумма 58.29, получена {as_is}"
            allure.attach("Сумма заказа корректна ✓", name="Валидация суммы",
                         attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("Сумма заказа не получена", name="Ошибка",
                         attachment_type=allure.attachment_type.TEXT)

    with allure.step("7. Закрытие браузера"):
        browser.quit()
        allure.attach("Браузер закрыт", name="Завершение",
                     attachment_type=allure.attachment_type.TEXT)





