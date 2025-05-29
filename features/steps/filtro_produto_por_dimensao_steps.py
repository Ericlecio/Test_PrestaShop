import time
from behave import given, when, then
from features.pages import filtro_produto_por_dimensao_page as filtro

@given(u'usuário acessa o site')
def acessar_site(context):
    filtro.acessar_site()


@when(u'clica em ART na navbar')
def clicar_em_ART_Navbar(context):
    filtro.clicar_botao_art()


@when(u'seleciona a dimensão 40x60')
def selecionar_dimensao(context):
    filtro.selecionar_dimensao_40_60()


@then(u'devem ser exibidos 3 produtos com essa dimensão')
def step_impl(context):
    filtro.verificar_quantidade_produtos()
    