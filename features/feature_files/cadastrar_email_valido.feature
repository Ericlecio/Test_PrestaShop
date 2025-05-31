Funcionalidade: Cadastrar um email válido na aba de receber novidades

    @EJ
    Cenário: Exibir um alerta de inscrição efetuada com sucesso
        Dado que a página do prestashop seja acessada
        Quando o usuário digita um endereço de email válido "ejs@gmail.com"
        E clica no botão inscrever-se
        Então um alerta deve ser exibido informando "You have successfully subscribed to this newsletter."