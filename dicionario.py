dic_db = {}          #banco de dados
dic_cliente = dict()
dic_produto = dict()
dic_pedido =  dict()

def cadastrar_cliente():
  print("cadastrar cliente")
  id_cliente = int(input("Digite o id do cliente: "))
  nome_cliente = input("Digite o nome do cliente: ")
  endereco_cliente = input("Digite o endereco do cliente: ")
  telefone_cliente = input( "Digite o telefone do cliente: ")
  dic_cliente[id_cliente] = [nome_cliente,endereco_cliente,telefone_cliente] #a chave tem como valor , um registro.
  dic_db["cliente"] = dic_cliente
  print(dic_db)

def consultar_cliente():
  print("consultar cliente")
  nome_cliente = input("Digite o nome do cliente: ")
  buscar_cliente = dic_db['cliente']
  print(buscar_cliente)
  for id_cliente,dados_cliente in buscar_cliente.items(): #esse for quer dizer que eu vou percorrer cada item que ta dentro do buscar_cliente, e vai jogar a chave em id_cliente(primeira parte) e o valor em dados_cliente(segunda parte). O python faz isso naturalmente.
    #print(dados_cliente)                                 # o nome desse comportamento é "desempacotamento iterável", atrravés do método .items
    #print(id_cliente)
    if dados_cliente[0] == nome_cliente:
       for dados in dados_cliente:
         print(dados)

#OUTRA MANEIRA DE FAZER ESSA FUNÇÃO, melhorada por IA:

#def consultar_cliente():
#    print("--- CONSULTAR CLIENTE ---")
#    nome_busca = input("Digite o nome do cliente: ").strip()
#    for dados_cliente in dic_db["cliente"].values():
#        if dados_cliente[0] == nome_busca:
#           print("Dados do Cliente:")
#           print(f"Nome: {dados_cliente[0]}")
#           print(f"Endereço: {dados_cliente[1]}")
#           print(f"Telefone: {dados_cliente[2]}")
#           return
#   print("Cliente não encontrado!")


def atualizar_cliente():
  print("atualizar cliente")
  id_cliente = input("Digite o id do cliente: ")
  nome_cliente = input("Digite o nome do cliente: ")
  endereco_cliente = input("Digite o endereco do cliente: ")
  telefone_cliente = input( "Digite o telefone do cliente: ")
  dic_cliente[id_cliente] = [nome_cliente,endereco_cliente,telefone_cliente]
  dic_db["cliente"] = dic_cliente
  print(dic_db)


def excluir_cliente():
  print("excluir cliente")
  id_cliente = input("Digite o id do cliente: ")
  dic_cliente.pop(id_cliente)
  dic_db["cliente"] = dic_cliente
  print(dic_db)


def gerenciar_cliente():
  while True:
    print("1-cadastrar cliente")
    print("2-consultar cliente")
    print("3-atualizar cliente")
    print("4-excluir cliente")
    print("5-retornar")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
      cadastrar_cliente()
    elif opcao == 2:
      consultar_cliente()
    elif opcao == 3:
      atualizar_cliente()
    elif opcao == 4:
      excluir_cliente()

    else:
      break

def cadastrar_produto():
  print("cadastrar produto")
  id_produto = int(input("Digite o id do produto :"))
  nome_produto = input("Digite o nome do produto :")
  preco_produto = float(input("Digite o preço do produto :"))
  dic_produto[id_produto] = [nome_produto, preco_produto]
  dic_db["Produto"] = dic_produto
  print("Pedido:", dic_db["Produto"])

def consultar_produto():
  print("consultar produto")
  consultar_produto = input("Digite o nome do produto que deseja buscar : ")
  buscar_produto = dic_db["Produto"]
  for id_produto, dados_produto in buscar_produto.items():
   if dados_produto[0].lower() == consultar_produto.lower():
     print(f"Nome: {dados_produto[0]}")
     print(f"Preço: {dados_produto[1]:.2f}") #2f formata o numero para não ter muitos numeros dps da virgula.

def atualizar_produtos():
  print("atualizar produto")
  id_produto = int(input("Digite o ID do produto : "))
  nome_produto = input("Digiteo o nome do produto : ")
  preco_produto = input("Digite o preço do produto")
  dic_produto[id_produto] = [nome_produto, preco_produto]
  dic_db["Produto"] = dic_produto
  print("Dados atualizados: ", dic_db )

def excluir_produto():
  id_produto = int(input("Informe o id do produto para exclusao"))
  if id_produto in dic_produto:
    dic_produto.pop(id_produto)
    dic_db["Produto"] = dic_produto
    print("Produto:", dic_db["Produto"])





def gerenciar_produto():
   while True:
    print("1-cadastrar produto")
    print("2-consultar produto")
    print("3-atualizar produto")
    print("4-excluir produto")
    print("5-retornar")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
      cadastrar_produto()
    elif opcao == 2:
      consultar_produto()
    elif opcao == 3:
      atualizar_produto()
    elif opcao == 4:
      excluir_produto()




while True:
    print("MENU PRINCIPAL = GESTÃO DE VENDAS")
    print("1-cliente")
    print("2-produto")
    print("3-pedido")
    print("4-sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
      gerenciar_cliente()
    elif opcao == 2:
     gerenciar_produto()
    elif opcao == 3:
      print("pedido")
    else:
      break