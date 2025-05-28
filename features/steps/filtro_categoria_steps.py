from behave import given, when, then
from features.pages import filtro_categoria_page as filtro
import time

@given(u'que eu acesso o site "{url}"')
def step_acessar_site(context, url):
    filtro.acessar_site()

@when(u'eu clico no nome "{nome}" na navbar')
def step_clicar_nome_navbar(context, nome):
    if nome.lower() == "clothes":
        filtro.clicar_clothes()
    else:
        raise NotImplementedError(f"NavBar {nome} não implementado")

@when(u'eu clico na categoria "{categoria}"')
def step_clicar_categoria(context, categoria):
    if categoria.lower() == "men":
        filtro.clicar_men()
    else:
        raise NotImplementedError(f"Categoria {categoria} não implementada")


@then(u'os produtos da categoria MEN devem ser exibidos')
def step_verificar_categoria(context):
    time.sleep(3)
    pass
