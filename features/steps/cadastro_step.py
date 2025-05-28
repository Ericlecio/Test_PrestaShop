import time
from behave import given, when, then
from features.pages import cadastro_page as cadastro

@given(u'que o site PrestaShop Demo seja acessado')
def step_acessar_site(context):
    cadastro.acessar_site()

@given(u'que o usuário clique no botão Sign In')
def step_clicar_sign_in(context):
    cadastro.clicar_sign_in()
    time.sleep(3)

@given(u'que o usuário clique para criar uma nova conta')
def step_clicar_criar_conta(context):
    cadastro.clicar_criar_conta()
    time.sleep(3)


@given(u'que o usuário preencha todos os campos obrigatórios do cadastro')
def step_preencher_todos_os_campos(context):
    cadastro.preencher_todos_os_campos()
    time.sleep(3)

@when(u'o usuário clicar no botão Save')
def step_clicar_save(context):
    cadastro.clicar_botao_save()
    time.sleep(3)

@then(u'o sistema deverá registrar o usuário com sucesso')
def step_verificar_cadastro(context):
    assert cadastro.verificar_cadastro_sucesso(), "Cadastro não realizado com sucesso!"
