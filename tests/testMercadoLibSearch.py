import unittest
from selenium import webdriver
from page_objects.homePageItems import HomePageItems
from page_objects.listItemsPage import ListItemsPage


class searchMeLiCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.mercadolibre.com.ar/')
        self.itemHomePage = HomePageItems(self.driver)
        self.listItemsPage = ListItemsPage(self.driver)

    def test_buscar_nintendo(self):
        self.itemHomePage.buscar_producto('nintendo gamecube')
        self.assertEqual(self.listItemsPage.return_resultado_busqueda(), 'Nintendo gamecube')
        self.driver.execute_script("window.scrollTo(0, 200)")
        self.listItemsPage.filtrar_por_consola()
        self.listItemsPage.filtrar_por_marca()
        self.listItemsPage.filtrar_por_modelo()
        self.listItemsPage.obtener_resultados()
        self.assertIn('Nintendo Gamecube', self.listItemsPage.obtener_resultados())



    def tearDown(self):
        self.driver.quit()
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()