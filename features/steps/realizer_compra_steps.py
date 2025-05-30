import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.realizar_compra_page import *

# @given(u'que a página de treinamento seja acessada')
# def acessar_site_treinamento(context):
#     get_driver().get("https://demo.prestashop.com/#/en/front")
#     time.sleep(15)
    

@when(u'o úsuario realizar uma compra')
def preencher_campos_obrigatorios(context):
    clicar_produto()
    
@then(u'o produto deve aparecer no carrinho')
def verificar_produto_no_carrinho_step(context):
    assert verificar_produto_no_carrinho()
