from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HeaderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_cart(self):
        cart_btn = self.wait.until(EC.element_to_be_clickable((By.ID, 'cart')))
        cart_btn.click()
        view_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//strong[text()=" View Cart"]')))
        view_cart.click()