from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class CrearCuentaPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        self.input_nombre = (By.NAME, 'firstName')
        self.input_apellido = (By.NAME, 'lastName')
        self.input_dni = (By.NAME, 'identification')
        self.input_email = (By.NAME, 'email')
        self.input_clave = (By.NAME, 'password')
        self.checkbox_aceptar = (By.ID, 'tyc_checkbox')
        self.checkbox_aceptar_span = (By.XPATH, '//*[@id="root-app"]/div/div/form/div[1]/div[5]/label/span[2]')
        self.disclaimer_button = (By.ID, 'cookieDisclaimerButton')
        self.check_captcha = (By.CLASS_NAME, 'recaptcha-checkbox-border')
        self.boton_continuar = (By.XPATH, '//*[@id="root-app"]/div/div/form/div[2]/button/span')

    def acepatar_cookies(self):
        self.driver.find_element(*self.disclaimer_button).click()

    def completar_nombre(self, keys):
        self.driver.find_element(*self.input_nombre).send_keys(keys)

    def completar_apellido(self, keys):
        self.driver.find_element(*self.input_apellido).send_keys(keys)

    def completar_dni(self, keys):
        self.driver.find_element(*self.input_dni).send_keys(keys)

    def completar_email(self, keys):
        self.driver.find_element(*self.input_email).send_keys(keys)

    def completar_clave(self, keys):
        self.driver.find_element(*self.input_clave).send_keys(keys)

    def click_checkbox(self):
        self.driver.find_element(*self.checkbox_aceptar_span).click()
        self.driver.find_element(*self.checkbox_aceptar).click()

    #def click_checkbox_captcha(self):
    #    self.driver.find_element(*self.check_captcha).click()
