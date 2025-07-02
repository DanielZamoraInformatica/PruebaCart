from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'button-cart')))
        add_button.click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-success')))