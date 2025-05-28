from behave import given, when, then # type: ignore
from features.pages import wishlist_page as wishlist

@given(u'que o usuário já esteja logado no sistema')
def step_usuario_logado(context):
    context.execute_steps('''
        Given que o site PrestaShop Demo seja acessado
        Given que o usuário clique no botão Sign In
        Given que o usuário clique para criar uma nova conta
        Given que o usuário preencha todos os campos obrigatórios do cadastro
        When o usuário clicar no botão Save
        Then o sistema deverá registrar o usuário com sucesso
    ''')

@when(u'eu escolho o primeiro produto e clico no ícone de coração para adicionar à lista de desejos')
def step_clicar_icone_coracao(context):
    wishlist.clicar_primeiro_produto_favorito()

@when(u'no modal "Add to wishlist" confirmo a adição do produto')
def step_confirmar_modal(context):
    wishlist.confirmar_adicao_wishlist()

@when(u'eu clico no meu nome na aba de notificações para acessar o perfil')
def step_clicar_nome_perfil(context):
    wishlist.clicar_nome_perfil()

@when(u'entro na página "My wishlists"')
def step_entrar_my_wishlists(context):
    wishlist.acessar_my_wishlists()

@then(u'o produto adicionado deve estar visível na lista de desejos')
def step_validar_produto_wishlist(context):
    assert wishlist.produto_esta_visivel(), "Produto não encontrado na lista de desejos"
