from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
import time

PRODUTO_TSHIRT = 'a.product-thumbnail[href*="hummingbird-printed-t-shirt"]'
ICONE_PINTEREST = 'li.pinterest a'

def acessar_site():
    get_driver().get("https://demo.prestashop.com/#/en/front")
    time.sleep(3)
    iframe = get_driver().find_element(By.TAG_NAME, "iframe")
    get_driver().switch_to.frame(iframe)

def clicar_no_produto():
    get_driver().find_element(By.CSS_SELECTOR, PRODUTO_TSHIRT).click()

def clicar_icone_pinterest():
    time.sleep(2)
    get_driver().find_element(By.CSS_SELECTOR, ICONE_PINTEREST).click()

def verificar_pagina_pinterest_aberta():
    driver = get_driver()
    time.sleep(2)
    janelas = driver.window_handles
    if len(janelas) < 2:
        return False
    driver.switch_to.window(janelas[1])
    return "pinterest.com" in driver.current_url
