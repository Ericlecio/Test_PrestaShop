import time
from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select

CAMPO_EMAIL = '//*[@id="blockEmailSubscription_displayFooterBefore"]/div/div/form/div/div[1]/div[1]/input'
BTN_INSCREVER_SE = 'input[name="submitNewsletter"]'
ALERTA_SUCESSO = 'p.alert'

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

def get_campo_email(email):
    entrar_no_iframe()
    return get_driver().find_element(By.XPATH, CAMPO_EMAIL).send_keys(email)

def click_btn_inscrever_se():
    find_element(BTN_INSCREVER_SE).click()

def get_alerta_sucesso(alerta):
    texto_alerta = find_element(ALERTA_SUCESSO).text
    assert texto_alerta == alerta, f"Mensagem do alerta{texto_alerta} diferente do {alerta}"