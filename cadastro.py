dic_alunos = dict()

def cadastrar_aluno():
  lista_dados_aluno = []

  matricula = input("Digite a matricula do aluno: ")
  nome = input("Digite o nome do aluno: ")
  cpf = input("Digite o cpf do aluno: ")
  telefone = input("Digite o telefone do aluno: ")

  lista_dados_aluno = [nome, cpf, telefone]

  dic_alunos[matricula] = lista_dados_aluno


def listar_alunos():
  for matricula, nome in dic_alunos.items():
    print(f"Matricula: {matricula} - Nome: {nome}")

def buscar_aluno():
  nome = input("Digite o nome do aluno: ")

  for lista in dic_alunos.values():
    if nome in lista:
      print(f"Nome: {lista[0]}")
      print(f"CPF: {lista[1]}")
      print(f"Telefone: {lista[2]}")


def excluir_aluno():
  matricula = input("Digite a matricula do aluno: ")
  if matricula in dic_alunos:
    del dic_alunos[matricula]
    print("Aluno excluido com sucesso")
  else:
    print("Aluno não encontrado")


def alterar_aluno():
  matricula = input("Digite a matricula do aluno: ")
  if matricula in dic_alunos:
    print("Nome: ", dic_alunos[matricula])
    nome = input("Digite o novo nome do aluno: ")
    dic_alunos[matricula] = nome

  print("CADASTRO DE ALUNOS")
while True:
  print("1 - CADASTRAR ALUNO")
  print("2 - LISTAR ALUNO")
  print("3 - BUSCAR ALUNO")
  print("4 - EXCLUIR ALUNO")
  print("5 - ALTERAR ALUNO")
  print("6 - SAIR")

  opcao = input("Escolha uma opção: ")
  if opcao == "1":
     print("Cadastrar aluno")
     cadastrar_aluno()
  elif opcao == "2":
    print("Listar aluno")
    listar_alunos()
  elif opcao == "3":
    print("Buscar aluno")
    buscar_aluno()
  elif opcao == "4":
    print("Excluir aluno")
    excluir_aluno()
  elif opcao == "5":
    print("Alterar aluno")
    alterar_aluno()
  elif opcao == "6":
      print("Saindo do programa")
      break
  else:
      print("Opção inválida")
