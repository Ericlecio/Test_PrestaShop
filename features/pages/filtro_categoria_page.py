from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL_SITE = "https://demo.prestashop.com/#/en/front"

LINK_CLOTHES = "a.dropdown-item[href*='3-clothes']"
LINK_MEN = "a.subcategory-name[href*='4-men']"
TITULO_CATEGORIA = "h1.h1"

def acessar_site():
    driver = get_driver()
    driver.get(URL_SITE)
    time.sleep(5)

def entrar_no_iframe():
    driver = get_driver()
    driver.switch_to.default_content()
    iframe = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

def clicar_clothes():
    driver = get_driver()
    entrar_no_iframe()
    clothes = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, LINK_CLOTHES))
    )
    clothes.click()
    time.sleep(3)

def clicar_men():
    driver = get_driver()
    driver.switch_to.default_content()
    entrar_no_iframe()

    men = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, LINK_MEN))
    )
    men.click()
    print("[DEBUG] Clicou no link MEN")

    # Agora verificar imediatamente o título da categoria
    titulo = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, TITULO_CATEGORIA))
    )
    texto_titulo = titulo.text.strip()
    print(f"[DEBUG] Título categoria após clique em MEN: '{texto_titulo}'")
    if "MEN" not in texto_titulo:
        raise Exception("Após clicar em MEN, a categoria MEN não está exibida")

def verificar_categoria_men():
    driver = get_driver()
    entrar_no_iframe()
    titulo = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1"))
    )
    print(f"[DEBUG] Título categoria: '{titulo.text.strip()}'")
    return "Men" in titulo.text.strip()
