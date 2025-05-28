from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL_PRINCIPAL = "https://demo.prestashop.com/#/en/front"

PRIMEIRO_PRODUTO = "article.product-miniature.js-product-miniature"
LINK_PRODUTO = "h3.product-title a"
FOTO_PRODUTO = "div.layer[data-toggle='modal']"  

def acessar_pagina_inicial():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    time.sleep(5) 

def entrar_no_iframe():
    driver = get_driver()
    driver.switch_to.default_content()
    iframe = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

def clicar_produto_desejado():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    entrar_no_iframe()
    produto_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((
            By.XPATH, "//h3[contains(@class, 'product-title')]/a[contains(text(), 'Hummingbird printed t-shirt')]"
        ))
    )
    produto_link.click()
    time.sleep(5)

def clicar_foto_produto():
    driver = get_driver()
    entrar_no_iframe()
    foto = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, FOTO_PRODUTO))
    )
    foto.click()
    time.sleep(5)  

def modal_esta_aberto():
    driver = get_driver()
    entrar_no_iframe()
    modal = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "product-modal"))
    )
    classes = modal.get_attribute("class")
    return "in" in classes.split()

def imagem_ampliada_exibida():
    try:
        return modal_esta_aberto()
    except Exception as e:
        print(f"Erro ao verificar modal aberto: {e}")
        return False
