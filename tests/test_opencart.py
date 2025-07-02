import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import allure

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.header_page import HeaderPage

class TestOpenCartFlow(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://opencart.abstracta.us/")
        self.driver.maximize_window()

    @allure.story("Agregar y eliminar producto del carrito")
    def test_shopping_cart_flow(self):
        with allure.step("Buscar producto 'iPhone'"):
            home = HomePage(self.driver)
            home.search_product("iPhone")
            self._attach_screenshot("Busqueda de producto")

        with allure.step("Seleccionar primer resultado de búsqueda"):
            results = SearchResultsPage(self.driver)
            product_name = results.select_first_product()
            self._attach_screenshot("Detalle del producto")

        with allure.step("Agregar producto al carrito"):
            product = ProductPage(self.driver)
            product.add_to_cart()
            self._attach_screenshot("Producto agregado al carrito")

        with allure.step("Ir al carrito de compras"):    
            header = HeaderPage(self.driver)
            header.go_to_cart()
            self._attach_screenshot("Vista del carrito")

        with allure.step("Validar producto en carrito"):
            cart = CartPage(self.driver)
            self.assertTrue(cart.validate_product_in_cart(product_name), "Producto no encontrado en el carrito")
            self._attach_screenshot("Validación del producto en carrito")

        with allure.step("Eliminar producto del carrito"):
            cart.remove_product()
            self._attach_screenshot("Producto eliminado del carrito")

        with allure.step("Validar carrito vacío"):
            self.assertTrue(cart.is_cart_empty(), "El carrito aún contiene productos")
            self._attach_screenshot("Carrito vacío")
    
    def _attach_screenshot(self, name="screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()