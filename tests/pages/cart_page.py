from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")

    def start_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/cart.html")
        )

        checkout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT)
        )

        checkout.click()