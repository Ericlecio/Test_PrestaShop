Funcionalidade: Alterar quantidade de itens 

    @EJ
    Cenário: Alterar quantidade de itens do carrinho para 2
        Dado que a página do site prestashop seja acessada
        Quando o usuario clicar em um produto listado
        E alterar a quantidade do produto para 2
        E clica no botão adicionar
        Então deve ser exibida uma janela informando "Product successfully added to your shopping cart"
        E deve aparecer a mensagem "There are 2 items in your cart."