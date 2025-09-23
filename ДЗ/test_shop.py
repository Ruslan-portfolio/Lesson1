from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from page_shop.Auth import Auth
from page_shop.MainPage import MainPage
from page_shop.Cart import Cart
from page_shop.Filling_in_data import Data
from page_shop.Total import Total

def test_shopping():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    auth_page = Auth(browser)
    auth_page.auth("standard_user", "secret_sauce")
    sleep(1)
    auth_page.submit()

    main_page = MainPage(browser)
    main_page.add_products()
    main_page.go_to_the_cart()

    cart_page = Cart(browser)
    cart_page.submit()

    data_page = Data(browser)
    data_page.filling_in_data("Иван", "Петров", "123456")
    data_page.submit()

    total_page = Total(browser)
    as_is = total_page.total()

    assert as_is == "58.29"

    browser.quit()





