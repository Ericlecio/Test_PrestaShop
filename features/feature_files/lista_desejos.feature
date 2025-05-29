Funcionalidade: Lista de Desejos

Contexto:
  Dado que o site PrestaShop Demo seja acessado
  E que o usuário clique no botão Sign In
  E que o usuário clique para criar uma nova conta
  E que o usuário preencha todos os campos obrigatórios do cadastro
  Quando o usuário clicar no botão Save
  Então o sistema deverá registrar o usuário com sucesso

@ET
Cenário: Adicionar produto à lista de desejos e visualizar na My Wishlists
  Quando eu escolho o primeiro produto e clico no ícone de coração para adicionar à lista de desejos
  E no modal "Add to wishlist" confirmo a adição do produto
  E eu clico no meu nome na aba de notificações para acessar o perfil
  E entro na página "My wishlists"
  E eu clico no item "My wishlist" na lista de desejos
  Então o produto adicionado é mostrado
