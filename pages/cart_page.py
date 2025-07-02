from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def validate_product_in_cart(self, product_name):
        item = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table-responsive .text-left a')))
        return product_name.lower() in item.text.lower()

    def remove_product(self):
        remove_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-original-title="Remove"]')))
        remove_btn.click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#content'), 'Your shopping cart is empty!'))

    def is_cart_empty(self):
        return 'Your shopping cart is empty!' in self.driver.page_source