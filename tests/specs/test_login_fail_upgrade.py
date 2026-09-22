import pytest
from guara.application import Application
from selenium.webdriver.common.by import By

from tests.fixtures.driver import driver
from tests.transactions.login_transaction import LoginTransaction


@pytest.mark.smoke
def test_login_fail(driver):

    app = Application(driver)

    app.given(
        LoginTransaction,
        url="https://www.saucedemo.com",
        user="usuario_invalido",
        password="senha_invalida",
    )

    mensagem_erro = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert mensagem_erro.is_displayed()
    assert (
        "Epic sadface: Username and password do not match any user in this service"
        in mensagem_erro.text
    )