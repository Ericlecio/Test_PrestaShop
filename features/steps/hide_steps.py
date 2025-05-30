import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.hide_page import *

@given(u'que a página de treinamento seja acessada')
def acessar_site_treinamento(context):
    get_driver().get("https://demo.prestashop.com/#/en/front")
    time.sleep(15)
    

@when(u'o úsuario clicar no botão hide')
def preencher_campos_obrigatorios(context):
    clicar_hide()
    

@then("o botao show deve aparecer")
def step_impl(context):
    from features.pages.hide_page import elemento_visivel, BOTAO_SHOW
    assert elemento_visivel(BOTAO_SHOW), "Botão Show não está visível como esperado"
