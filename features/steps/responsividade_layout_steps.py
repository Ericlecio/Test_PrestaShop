import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages import responsividade_layout_page as responsi

@given(u'o usuário acessa o site')
def acessar_site(context):
    responsi.acessar_site()

@when(u'o usuário redimensiona a janela do navegador')
def redimensiona_para_tablet(context):
    responsi.clicar_botao_tablet()
    time.sleep(2)

@then(u'o conteúdo deve ajustar corretamente sua largura e altura')
def verificar_as_dimencoes(context):
    responsi.verificar_dimensao()