import pytest
from guara import it
from guara.application import Application

from tests.fixtures.driver import driver
from tests.transactions.login_transaction import LoginTransaction


@pytest.mark.smoke
def test_login_sucess(driver):

    app = Application(driver)

    app.given(
        LoginTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(it.Contains, "inventory")