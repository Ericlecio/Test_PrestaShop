from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.common.by import By
import time

##################################################### MAPEANDO CAMPOS NA TELA #####################################################

BOTAO_SIGN_IN = 'a[title="Log in to your customer account"]'
BOTAO_CRIAR_CONTA = 'a[data-link-action="display-register-form"]'
RADIO_TITULO_SR = "#field-id_gender-1"
CAMPO_NOME = "#field-firstname"
CAMPO_SOBRENOME = "#field-lastname"
CAMPO_EMAIL = "#field-email"
CAMPO_SENHA = "#field-password"
CAMPO_DATA_NASC = "#field-birthday"
CHECKBOX_TERMO = "input[name='psgdpr']"
CHECKBOX_PRIVACIDADE = "input[name='customer_privacy']"
BOTAO_SAVE = "button[data-link-action='save-customer']"
LINK_CONTA = "a.account"


nome = "Ericlecio"
sobrenome = "Morais"
email = f"ericlecio{int(time.time())}@discente.ifpe.edu.br"
senha = "StrongPass123@"
data_nasc = "01/01/1990"


def acessar_site():
    get_driver().get("https://demo.prestashop.com/#/en/front")
    time.sleep(3)
    iframe = get_driver().find_element(By.TAG_NAME, "iframe")
    get_driver().switch_to.frame(iframe)

def clicar_sign_in():
    find_element(BOTAO_SIGN_IN).click()

def clicar_criar_conta():
    find_element(BOTAO_CRIAR_CONTA).click()

def preencher_titulo():
    find_element(RADIO_TITULO_SR).click()

def preencher_nome():
    find_element(CAMPO_NOME).send_keys(nome)

def preencher_sobrenome():
    find_element(CAMPO_SOBRENOME).send_keys(sobrenome)

def preencher_email():
    find_element(CAMPO_EMAIL).send_keys(email)

def preencher_senha():
    find_element(CAMPO_SENHA).send_keys(senha)

def preencher_data_nascimento():
    find_element(CAMPO_DATA_NASC).send_keys(data_nasc)

def aceitar_termos():
    find_element(CHECKBOX_TERMO).click()

def aceitar_privacidade():
    find_element(CHECKBOX_PRIVACIDADE).click()

def clicar_botao_save():
    find_element(BOTAO_SAVE).click()

def verificar_cadastro_sucesso():
    return find_element(LINK_CONTA).is_displayed()

def preencher_todos_os_campos():
    preencher_titulo()
    preencher_nome()
    preencher_sobrenome()
    preencher_email()
    preencher_senha()
    preencher_data_nascimento()
    aceitar_termos()
    aceitar_privacidade()

