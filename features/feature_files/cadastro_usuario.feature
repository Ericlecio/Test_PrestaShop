Funcionalidade: Cadastro de usuário no PrestaShop

    Contexto:
        Dado que o site PrestaShop Demo seja acessado
        E que o usuário clique no botão Sign In
        E que o usuário clique para criar uma nova conta
        E que o usuário preencha todos os campos obrigatórios do cadastro

    @teste
    Cenário: Realizar cadastro com sucesso
        Quando o usuário clicar no botão Save
        Então o sistema deverá registrar o usuário com sucesso

