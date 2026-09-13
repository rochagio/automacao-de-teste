from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_foo():
    # Inicializa o ChromeDriver automaticamente
    driver = webdriver.Chrome()

    try:
        # 1. Abre a URL inicial
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        time.sleep(2)  # Pausa apenas para você visualizar a ação

        driver.find_element(By.ID, "my-text-id").send_keys("foo")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[2]/button").click()
        time.sleep(5)

    finally:
        # Fecha o navegador e encerra o processo
        driver.quit()
