from behave import given, when, then
from features.pages import product_page as product

@given(u'que eu estou na página inicial do site')
def step_abrir_pagina_inicial(context):
    product.acessar_pagina_inicial()

@when(u'eu clico no produto desejado para abrir a página do produto específico')
def step_clicar_produto(context):
    product.clicar_produto_desejado()

@when(u'clico na foto do produto')
def step_clicar_foto(context):
    product.clicar_foto_produto()

@then(u'a imagem do produto deve ser exibida em modo ampliado')
def step_validar_imagem_ampliada(context):
    assert product.imagem_ampliada_exibida(), "Imagem ampliada não exibida"

