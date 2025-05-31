import time
from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select

PRIMEIRO_PRODUTO = '//*[@id="content"]/section[1]/div/div[1]/article/div/div[1]/a'
BTN_AUMENTAR_QUANT = '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[1]/div/span[3]/button[1]'
BTN_ADICIONAR = '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button'
ALERTA_PRODUTO_ADD = '#myModalLabel'
QUANT_PRODUTO_DOIS = '.cart-content > p' 

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

def click_primeiro_produto():
    entrar_no_iframe()
    get_driver().find_element(By.XPATH, PRIMEIRO_PRODUTO).click()

def click_btn_aumentar_quant():
    get_driver().find_element(By.XPATH, BTN_AUMENTAR_QUANT).click()

def click_btn_adicionar():
    get_driver().find_element(By.XPATH, BTN_ADICIONAR).click()
    time.sleep(5)

def get_msg_produto_add(msg):
    mensagem = find_element(ALERTA_PRODUTO_ADD).text
    assert mensagem == msg, f"Mensagem do alerta {mensagem} diferente do {msg}"

def get_msg_dois_itens(msg):
    time.sleep(5)
    mensagem = find_element(QUANT_PRODUTO_DOIS).text
    assert mensagem == msg, f"Mensagem do alerta {mensagem} diferente do {msg}"
