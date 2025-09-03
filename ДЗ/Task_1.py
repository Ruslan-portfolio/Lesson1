from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")

WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#ajaxButton"))).click()


txt = WebDriverWait(driver, 17).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
        ).text
print(txt)

driver.quit()
