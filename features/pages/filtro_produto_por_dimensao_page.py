from selenium.webdriver.common.by import By
from features.helpers.driver import get_driver
import time
from features.pages.base_page import *

BOTAO_ART = "li#category-9.category a.dropdown-item"
DIV_PRINCIPAL = "#search_filters"
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
    time.sleep(3)

def clicar_botao_art():
    entrar_no_iframe()
    find_element(BOTAO_ART).click()
    time.sleep(2)

def selecionar_dimensao_40_60():
    entrar_no_iframe()
    divpai = find_element(DIV_PRINCIPAL)
    sections = divpai.find_elements(By.TAG_NAME, "section")
    quinta_section = sections[4] 
    ul = quinta_section.find_element(By.TAG_NAME, "ul")
    first_li = ul.find_elements(By.TAG_NAME, "li")[0]
    first_a = first_li.find_element(By.TAG_NAME, "a")
    first_a.click()
    time.sleep(2)

def verificar_quantidade_produtos():
    divpaiprodutos = find_element(DIV_PRODUTOS)
    divs = divpaiprodutos.find_elements(By.CSS_SELECTOR, ".js-product.product")
    quantidade_produtos = len(divs)
    assert quantidade_produtos == 3, f"Esperado 3 produtos, mas foram encontrados {quantidade_produtos}."
