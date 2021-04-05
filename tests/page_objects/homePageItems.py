from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePageItems:

    def __init__(self, driver):
        self.driver = driver
        self.boton_crear_cuenta = (By.XPATH, '//*[@id="nav-header-menu"]/a[1]')
        self.search_bar = (By.NAME, 'as_word')
        self.search_icon = (By.CLASS_NAME, 'nav-icon-search')
        self.aceptar_cookies = (By.XPATH, '//*[@id="cookieDisclaimerButton"]')

    def click_aceptar_cookies(self):
        self.driver.find_element(*self.aceptar_cookies).click()

    def click_crear_cuenta(self):
        self.driver.find_element(*self.boton_crear_cuenta).click()

    def buscar_producto(self, producto):
        self.driver.find_element(*self.search_bar).send_keys(producto)
        self.driver.find_element(*self.search_icon).click()