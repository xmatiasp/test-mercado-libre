import unittest
from selenium import webdriver
from page_objects.homePageItems import HomePageItems
from page_objects.crearCuentaPageItem import CrearCuentaPage
from pyunitreport import HTMLTestRunner
import time

class LoginMercadoLibreCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.mercadolibre.com.ar/')
        self.itemsHomePage = HomePageItems(self.driver)
        self.crearCuentaObj = CrearCuentaPage(self.driver)

    def test_login_correct(self):
        self.itemsHomePage.click_crear_cuenta()
        self.crearCuentaObj.acepatar_cookies()
        self.crearCuentaObj.completar_nombre('Matias Ezequiel')
        self.crearCuentaObj.completar_apellido('Palacio')
        self.crearCuentaObj.completar_email('matias@gmaol.com')
        self.crearCuentaObj.completar_dni('33333333')
        self.crearCuentaObj.completar_clave('123456')
        time.sleep(7)
        self.crearCuentaObj.click_checkbox()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()