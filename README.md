# PruebaCart
Prueba de carrito de compras en POM con evidencias y reporteria en allure

Para ejecutar una vez clonado el repositorio, se debe ejecutar el comando:

  python -m pytest tests/ --alluredir=allure-results (Esto creara la carpeta de los reportes allure)

Posteriormente para ver las evidencias con las pruebas ejecutadas y el paso a paso ejecutamos:

  allure serve allure-results
