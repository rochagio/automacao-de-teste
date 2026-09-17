import pytest
from selenium.webdriver.common.by import By

from tests.fixtures.driver import driver


@pytest.mark.smoke
def test_login_sucess(driver):

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url