from features.helpers.driver import get_driver
import time
from features.pages.base_page import *

BOTAO_TABLET = "a.change-device.tablet-h"
HTML_PRINCIPAL = '/html'

def acessar_site():
    get_driver().get("https://demo.prestashop.com/#/en/front")
    time.sleep(3)

def clicar_botao_tablet():
    elemento = find_element(BOTAO_TABLET)
    elemento.click()

def verificar_dimensao():
    driver = get_driver()
    iframe = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)

    elemento = get_driver().find_element(By.XPATH, HTML_PRINCIPAL)
    dimensao = elemento.size

    assert dimensao['width'] >= 1000
    assert dimensao['height'] >= 760
    
