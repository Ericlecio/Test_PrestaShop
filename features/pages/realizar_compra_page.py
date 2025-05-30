from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time


URL_PRINCIPAL = "https://demo.prestashop.com/#/en/front"
PRIMEIRO_PRODUTO = "article.product-miniature.js-product-miniature"
LINK_PRODUTO = "h3.product-title a"

def clicar_produto():
    acessar_pagina_inicial()
    entrar_no_iframe()
    clicar_produto_desejado()
    clicar_tamanho()
    clicar_comprar()
    confirmar_compra()
    
def acessar_pagina_inicial():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    time.sleep(5)

def entrar_no_iframe():
    driver = get_driver()
    driver.switch_to.default_content()
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

def clicar_produto_desejado():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    entrar_no_iframe()
    produto_link = driver.find_element(By.XPATH, "//h3[contains(@class, 'product-title')]/a[contains(text(), 'Hummingbird printed t-shirt')]")
    produto_link.click()
    time.sleep(5)
    
def clicar_tamanho():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    entrar_no_iframe()
    dropdown_element = driver.find_element(By.ID, "group_1")        
    select = Select(dropdown_element)
    select.select_by_value("3")
    time.sleep(5)
    
def clicar_comprar():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    entrar_no_iframe()
    produto_link = driver.find_element(By.XPATH, "//div[contains(@class, 'add')]/button[contains(@class, 'add-to-cart')]")
    produto_link.click()
    time.sleep(5)

def confirmar_compra():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    entrar_no_iframe()
    produto_link = driver.find_element(By.CSS_SELECTOR, '.modal-content a.btn.btn-primary[href*="action=show"]')
    produto_link.click()    
    time.sleep(5)

def verificar_produto_no_carrinho():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)
    try:
        xpath = "//a[@class='label' and contains(text(), 'Hummingbird printed t-shirt')]"
        elemento = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return elemento.is_displayed()
    except TimeoutException:
        return False

