from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ListItemsPage:
    def __init__(self, driver):
        self.driver = driver
        self.resultado_busqueda = (By.CLASS_NAME, 'ui-search-breadcrumb__title')
        self.categoria_consola = (By.XPATH, '//*[@id="root-app"]/div/div[1]/aside/section/dl[3]/dd[2]/a/span[1]')
        self.categoria_marca = (By.XPATH, '//*[@id="root-app"]/div/div[1]/aside/section/dl[2]/dd[1]/a/span[1]')
        self.categoria_modelo = (By.XPATH, '//*[@id="root-app"]/div/div[1]/aside/section/dl[2]/dd[2]/a/span[1]')



    def filtrar_por_consola(self):
        self.driver.find_element(*self.categoria_consola).click()

    def filtrar_por_marca(self):
        self.driver.find_element(*self.categoria_marca).click()

    def filtrar_por_modelo(self):
        self.driver.find_element(*self.categoria_modelo).click()

    def return_resultado_busqueda(self):
        return self.driver.find_element(*self.resultado_busqueda).text

    def obtener_resultados(self):
        articulo = []
        precio = []

        for i in range(5):
            nombre_articulo = self.driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articulo.append(nombre_articulo)
            precio_articulo = self.driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div/div/div/span[1]/span[2]').text
            precio.append(precio_articulo)
        print(articulo)
        #print(precio)

        return articulo