from behave import given, then, when
from selenium.webdriver.common.by import By

from tests.pages.inventory_page import InventoryPage
from tests.pages.login_page import LoginPage


@given("que o usuário acessa a página de login")
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when("ele realiza login com usuário válido")
def step_valid_login(context):
    context.login_page.login(
        "standard_user",
        "secret_sauce"
    )


@then("ele deve ser redirecionado para a página de inventário")
def step_validate_inventory(context):
    inventory_page = InventoryPage(context.driver)
    assert inventory_page.is_loaded()


@when("ele realiza login com usuário inválido")
def step_invalid_login(context):

    context.login_page.login(
        "usuario_invalido",
        "senha_invalida"
    )


@then("ele deve visualizar mensagem de erro")
def step_validate_invalid_login_error(context):

    mensagem = context.driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert mensagem.is_displayed()

    assert (
        "Username and password do not match any user in this service"
        in mensagem.text
    )


@when('ele realiza login com usuário "locked_out_user" e senha "secret_sauce"')
def step_locked_user_login(context):

    context.login_page.login(
        "locked_out_user",
        "secret_sauce"
    )


@then("ele deve visualizar mensagem de usuário bloqueado")
def step_validate_locked_user_error(context):

    mensagem = context.driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    assert mensagem.is_displayed()

    assert (
        "Sorry, this user has been locked out."
        in mensagem.text
    )