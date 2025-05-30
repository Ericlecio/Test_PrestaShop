import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.clique_show_page import *

# @given(u'que a página de treinamento seja acessada')
# def acessar_site_treinamento(context):
#     get_driver().get("https://demo.prestashop.com/#/en/front")
#     time.sleep(15)
    

@when(u'úsuario clicar no botão hide')
def clicar_botao_banner(context):
    botao_hide()

@when(u'úsuario clicar no botão show')
def clicar_botao_banner(context):
    botao_show()  

@then("o botao hide deve aparecer")
def step_impl(context):
    from features.pages.clique_show_page import elemento_visivel, NOME_HIDE
    assert elemento_visivel(NOME_HIDE), "Botão HIDE não está visível como esperado"
