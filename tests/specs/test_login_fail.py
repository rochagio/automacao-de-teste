import pytest
from selenium.webdriver.common.by import By

from tests.fixtures.driver import driver


@pytest.mark.smoke
def test_login_fail(driver):

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_invalida")

    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert mensagem_erro.is_displayed()
    assert "Username and password do not match" in mensagem_erro.text