import time
from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_PRINCIPAL = "https://demo.prestashop.com/#/en/front"

PRIMEIRO_PRODUTO = "article.product-miniature.js-product-miniature"
ICONE_CORACAO = "button.wishlist-button-add"
MODAL_ADD_WISHLIST = "div.wishlist-chooselist"
CONFIRMAR_ADD = "ul.wishlist-list li.wishlist-list-item p"
NOME_PERFIL = "a.account"
LINK_MY_WISHLISTS = "a#wishlist-link"
WISHLIST_PRODUTO = "a.wishlist-list-item-link p.wishlist-list-item-title"

def acessar_pagina_principal():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    try:
        iframe = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        driver.switch_to.frame(iframe)
    except:
        pass
    time.sleep(10)

def clicar_primeiro_produto_favorito():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)
    time.sleep(10)
    primeiro_produto = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, PRIMEIRO_PRODUTO))
    )
    botao_coracao = primeiro_produto.find_element(By.CSS_SELECTOR, ICONE_CORACAO)
    botao_coracao.click()


def confirmar_adicao_wishlist():
    driver = get_driver()
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, MODAL_ADD_WISHLIST))
    )
    confirmar = modal.find_element(By.CSS_SELECTOR, CONFIRMAR_ADD)
    confirmar.click()

def clicar_nome_perfil():
    driver = get_driver()
    nome = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, NOME_PERFIL))
    )
    nome.click()

def acessar_my_wishlists():
    driver = get_driver()
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, LINK_MY_WISHLISTS))
    )
    link.click()

def produto_esta_visivel():
    driver = get_driver()
    try:
        # Espera o item aparecer na lista de desejos
        produto = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, WISHLIST_PRODUTO))
        )
        return True
    except:
        return False
