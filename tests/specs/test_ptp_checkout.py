import pytest
from guara import it
from guara.application import Application
from selenium import webdriver

from tests.fixtures.driver import driver
from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.checkout_transaction import CheckoutTransaction
from tests.transactions.finish_order_transaction import FinishOrderTransaction
from tests.transactions.login_transaction import LoginTransaction


@pytest.mark.smoke
def test_checkout_ptp(driver):
    app = Application(driver)

    app.given(
        LoginTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(it.Contains, "inventory")

    app.when(AddToCartTransaction).asserts(it.Contains, "cart")

    app.when(
        CheckoutTransaction, name="Douglas", last="Teste", zip_code="12345"
    ).asserts(it.Contains, "checkout-step-two")

    app.when(FinishOrderTransaction).asserts(it.Contains, "Thank you")
