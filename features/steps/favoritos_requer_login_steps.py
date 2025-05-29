from behave import given, when, then
from features.pages import favoritos_requer_login_page as favorito

@given(u'que o usuário acessa o site')
def acessar_site(context):
    favorito.acessar_site()


@when(u'clica no ícone de coração de um produto')
def clicar_icone_coração_no_produto(conext):
    favorito.clicar_botao_coracao()


@then(u'deve ser exibida uma mensagem solicitando login "{mensagem}"')
def verificar_mensagem_modal(context, mensagem):
    favorito.verificar_mensagem(mensagem)

