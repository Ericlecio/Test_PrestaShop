from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages import alterar_quant_produto_page as alterar_quant


@given(u'que a página do site prestashop seja acessada')
def acessar_site_prestashop(context):
    alterar_quant.acessar_site()


@when(u'o usuario clicar em um produto listado')
def clicar_primeiro_produto(context):
    alterar_quant.click_primeiro_produto()


@when(u'alterar a quantidade do produto para 2')
def clicar_btn_aumentar_quant(context):
    alterar_quant.click_btn_aumentar_quant()


@when(u'clica no botão adicionar')
def clicar_btn_adicionar(context):
    alterar_quant.click_btn_adicionar()


@then(u'deve ser exibida uma janela informando "{msg_produto_add}"')
def verificar_produto_adicionado(context, msg_produto_add):
   alterar_quant.get_msg_produto_add(msg_produto_add)


@then(u'deve aparecer a mensagem "{msg_quant_produto}"')
def verificar_quant_produto(context, msg_quant_produto):
    alterar_quant.get_msg_dois_itens(msg_quant_produto)