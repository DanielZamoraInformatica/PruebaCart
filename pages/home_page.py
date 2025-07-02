from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def search_product(self, product_name):
        search_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'search')))
        search_input.clear()
        search_input.send_keys(product_name)
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-default.btn-lg')
        search_button.click()