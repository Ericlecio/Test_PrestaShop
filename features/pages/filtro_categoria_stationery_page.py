from selenium.webdriver.common.by import By
from features.helpers.driver import get_driver
import time
from features.pages.base_page import *

BOTAO_CATEGORIA = '#category-6'
BOTAO_STATIONERY = '//*[@id="left-column"]/div[1]/ul/li[2]/ul/li[1]/a'
DIV_PRODUTOS = ".products.row"

def entrar_no_iframe():
    driver = get_driver()
    driver.switch_to.default_content()
    iframe = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

def acessar_site():
    get_driver().get("https://demo.prestashop.com/#/en/front")
    time.sleep(5)

def clicar_categoria():
    entrar_no_iframe()
    find_element(BOTAO_CATEGORIA).click()
    time.sleep(3)

def clicar_stationery():
    entrar_no_iframe()
    get_driver().find_element(By.XPATH, BOTAO_STATIONERY).click()
    time.sleep(3)

def verificacao_produtos_stationery():
    entrar_no_iframe()
    divpaiprodutos = find_element(DIV_PRODUTOS)
    divs_produtos = divpaiprodutos.find_elements(By.CSS_SELECTOR, ".js-product.product")
    produto1 = divs_produtos[0].find_element(By.CSS_SELECTOR, "div.product-description .h3.product-title a").text
    assert produto1 == "Mountain Fox Notebook", f"Espera-se 'Mountain Fox Notebook', mas foi encontrado {produto1}."
    produto2 = divs_produtos[1].find_element(By.CSS_SELECTOR, "div.product-description .h3.product-title a").text
    assert produto2 == "Brown Bear Notebook", f"Espera-se 'Brown Bear Notebook', mas foi encontrado {produto2}."
    produto3 = divs_produtos[2].find_element(By.CSS_SELECTOR, "div.product-description .h3.product-title a").text
    assert produto3 == "Hummingbird Notebook", f"Espera-se 'Hummingbird Notebook', mas foi encontrado {produto3}."
    