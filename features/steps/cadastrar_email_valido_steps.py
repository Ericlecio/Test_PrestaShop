import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages import cadastrar_email_valido_page as cadastrar_email


@given(u'que a página do prestashop seja acessada')
def acessar_site_prestashop(context):
    cadastrar_email.acessar_site()


@when(u'o usuário digita um endereço de email válido "{email_valido}"')
def inserir_campo_email(context, email_valido):
    cadastrar_email.get_campo_email(email_valido)
    time.sleep(2)


@when(u'clica no botão inscrever-se')
def clicar_btn_inscrever_se(context):
    cadastrar_email.click_btn_inscrever_se()


@then(u'um alerta deve ser exibido informando "{alerta_sucesso}"')
def verificar_alerta_sucesso(context, alerta_sucesso):
    cadastrar_email.get_alerta_sucesso(alerta_sucesso)