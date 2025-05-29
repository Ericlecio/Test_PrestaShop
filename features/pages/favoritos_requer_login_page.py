from features.helpers.driver import get_driver
import time
from features.pages.base_page import *

ICONE_CORACAO = "button.wishlist-button-add"
TEXTO_MODAL = '//*[@id="footer"]/div[2]/div/div[1]/div[7]/div[1]/div/div/div[2]/p'

def acessar_site():
    get_driver().get("https://demo.prestashop.com/#/en/front")
    time.sleep(3)

def entrar_no_iframe():
    driver = get_driver()
    driver.switch_to.default_content()
    iframe = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

def clicar_botao_coracao():
    entrar_no_iframe()
    botao_coracao = find_element(ICONE_CORACAO)
    botao_coracao.click()
    time.sleep(5)


def verificar_mensagem(mensagem):
    elemento_mensagem = get_driver().find_element(By.XPATH, TEXTO_MODAL)
    texto = elemento_mensagem.text.strip()
    assert texto == mensagem, f"Mensagem esperada: '{mensagem}', mas foi exibida: '{texto}'"