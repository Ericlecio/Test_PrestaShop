import time
from features.helpers.driver import get_driver
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
WISHLIST_ITEM = "li.wishlist-list-item-default a.wishlist-list-item-link p.wishlist-list-item-title"


def clicar_primeiro_produto_favorito():
    driver = get_driver()
    driver.get(URL_PRINCIPAL)
    iframe = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)
    time.sleep(3)  
    
    primeiro_produto = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, PRIMEIRO_PRODUTO)))
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", primeiro_produto)
    time.sleep(2) 
    
    botao_coracao = primeiro_produto.find_element(By.CSS_SELECTOR, ICONE_CORACAO)
    botao_coracao.click()
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'start'});", primeiro_produto)

def confirmar_adicao_wishlist():
    driver = get_driver()
    modal = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, MODAL_ADD_WISHLIST)))
    time.sleep(3)  
    confirmar = modal.find_element(By.CSS_SELECTOR, CONFIRMAR_ADD)
    confirmar.click()
    time.sleep(5)

def clicar_nome_perfil():
    driver = get_driver()
    nome = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, NOME_PERFIL)))
    time.sleep(3)
    nome.click()
    time.sleep(3) 

def acessar_my_wishlists():
    driver = get_driver()
    link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, LINK_MY_WISHLISTS)))
    time.sleep(3)
    link.click()
    time.sleep(3)

def produto_esta_visivel():
    driver = get_driver()
    try:
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.wishlist-product-image img[alt='Hummingbird printed t-shirt']"))
        )
        time.sleep(3)  
        return True
    except Exception as e:
        print(f"Erro: {e}")
        return False

def clicar_my_wishlist_item():
    driver = get_driver()
    elemento = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, WISHLIST_ITEM))
    )
    elemento.click()
    time.sleep(3)
    
    