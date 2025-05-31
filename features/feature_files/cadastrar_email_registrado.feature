Funcionalidade: Cadastrar um email registrado na aba de receber novidades

    @EJ
    Cenário: Exibir um alerta de email já registrado
        Dado que a página do prestashop esteja acessada
        Quando o usuário digita um endereço de email registrado "ejs@gmail.com"
        E clicar no botão de inscrever-se 
        Então um alerta deve ser exibido na página informando "This email address is already registered."