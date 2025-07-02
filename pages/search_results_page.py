from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def select_first_product(self):
        first_result = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-layout .caption a')))
        product_name = first_result.text
        first_result.click()
        return product_name