import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages import cadastrar_email_registrado_page as cadastrar_email_registrado


@given(u'que a página do prestashop esteja acessada')
def acessar_site_prestashop(context):
    cadastrar_email_registrado.acessar_site()


@when(u'o usuário digita um endereço de email registrado "{email_registrado}"')
def inserir_campo_email(context, email_registrado):
    cadastrar_email_registrado.get_campo_email(email_registrado)
    time.sleep(2)


@when(u'clicar no botão de inscrever-se')
def clicar_btn_inscrever_se(context):
    cadastrar_email_registrado.click_btn_inscrever_se()
    cadastrar_email_registrado.click_btn_inscrever_se()
    time.sleep(4)


@then(u'um alerta deve ser exibido na página informando "{alerta_registrado}"')
def verificar_alerta_email_registrado(context, alerta_registrado):
    cadastrar_email_registrado.get_alerta_email_registrado(alerta_registrado)