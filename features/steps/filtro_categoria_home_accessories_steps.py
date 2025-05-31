import time
from behave import given, when, then
from features.pages import filtro_categoria_home_accessories_page as filtro


@given(u'que o usuário está na página web principal')
def acessar_site(context):
    filtro.acessar_site()

@when(u'o usuário seleciona a categoria ACCESSORIES/HOME ACCESSORIES')
def clicar_categoria(context):
    filtro.clicar_categoria()
    filtro.clicar_home_accessories()

@then(u'o sistema deve exibir apenas os produtos pertencentes à categoria ACCESSORIES/HOME ACCESSORIES')
def step_impl(context):
    filtro.verificacao_produtos_home_accessories()
    