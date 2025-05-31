import time
from behave import given, when, then
from features.pages import filtro_categoria_stationery_page as filtro

@given(u'que o usuário está na página web')
def acessar_site(context):
    filtro.acessar_site()


@when(u'o usuário seleciona a categoria ACCESSORIES/STATIONERY')
def clicar_categoria(context):
    filtro.clicar_categoria()
    filtro.clicar_stationery()


@then(u'o sistema deve exibir apenas os produtos pertencentes à categoria ACCESSORIES/STATIONERY')
def verificar_produtos(context):
    filtro.verificacao_produtos_stationery()

