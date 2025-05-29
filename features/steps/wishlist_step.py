from behave import when, then # type: ignore
from features.pages import wishlist_page as wishlist

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

@when(u'eu clico no item "My wishlist" na lista de desejos')
def step_clicar_item_my_wishlist(context):
    wishlist.clicar_my_wishlist_item()

@then(u'o produto adicionado é mostrado')
def step_validar_produto_wishlist(context):
    assert wishlist.produto_esta_visivel(), "Produto não encontrado na lista de desejos"

