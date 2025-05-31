from behave import given, when, then
from features.pages import produto_pinterest_page as page
import time

@given("que acesso a página inicial para compartilhamento")
def step_acessar_site(context):
    page.acessar_site()

@when("eu escolho um produto")
def step_escolher_produto(context):
    pass

@when("clico no produto")
def step_clicar_produto(context):
    page.clicar_no_produto()
    time.sleep(3)

@when("clico no ícone do Pinterest")
def step_clicar_pinterest(context):
    page.clicar_icone_pinterest()
    time.sleep(3)

@then("a página do Pinterest deve ser aberta")
def step_verificar_pinterest(context):
    assert page.verificar_pagina_pinterest_aberta(), "A página do Pinterest não foi aberta corretamente"
