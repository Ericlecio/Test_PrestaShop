Funcionalidade: Lista de Desejos

  Background:
    Dado que o usuário já esteja logado no sistema

  Cenário: Adicionar produto à lista de desejos e visualizar na My Wishlists
    Quando eu escolho o primeiro produto e clico no ícone de coração para adicionar à lista de desejos
    E no modal "Add to wishlist" confirmo a adição do produto
    E eu clico no meu nome na aba de notificações para acessar o perfil
    E entro na página "My wishlists"
    Então o produto adicionado deve estar visível na lista de desejos
