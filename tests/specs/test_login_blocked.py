import pytest
from selenium.webdriver.common.by import By

from tests.fixtures.driver import driver


@pytest.mark.smoke
def test_login_blocked(driver):

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert mensagem_erro.is_displayed()
    assert "Sorry, this user has been locked out." in mensagem_erro.text