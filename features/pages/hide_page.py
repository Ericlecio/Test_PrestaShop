from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time


BOTAO_HIDE = "a.btn.btn-collapse"
BOTAO_SHOW = (By.CLASS_NAME, "show-header")

def clicar_hide():    
    clicar_botao_hide()
    
def clicar_botao_hide():
    find_element(BOTAO_HIDE).click()
    time.sleep(5)
    

def elemento_visivel(localizador):
    return WebDriverWait(get_driver(), 10).until(
        EC.visibility_of_element_located(localizador)
    )


