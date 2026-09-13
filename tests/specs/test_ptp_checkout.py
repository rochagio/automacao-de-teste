from guara.application import Application
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from guara import it
from tests.transactions.login_transaction import LoginTransaction
from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.checkout_transaction import CheckoutTransaction
from tests.transactions.finish_order_transaction import FinishOrderTransaction

@pytest.mark.smoke
def test_checkout_ptp():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        app = Application(driver)

        app = Application(webdriver.Chrome())
        app.given(
            LoginTransaction,
            url="https://www.saucedemo.com",
            user="standard_user",
            password="secret_sauce",
        ).then(it.Contains, "inventory")
        app.when(AddToCartTransaction).asserts(it.Contains, "cart")
        app.when(CheckoutTransaction, name="Douglas", last="Teste", zip_code="12345").asserts(
            it.Contains, "checkout-step-two"
        )
        app.when(FinishOrderTransaction).asserts(it.Contains, "Thank you")

    finally:
        driver.quit()