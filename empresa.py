salario = int(input("Digite seu salario:"))
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
dividas = input("Você possui dívidas com agiotas? (Sim ou Não):")

print("Seu salário é: R$%.2f" % salario)
print("Seu nome é:", nome)# Solicita ao usuário que insira seu salário como um número inteiro.
salario = int(input("Digite seu salario:"))

# Solicita ao usuário que insira seu nome como texto.
nome = input("Digite seu nome:")

# Solicita ao usuário que insira sua idade como um número inteiro.
idade = int(input("Digite sua idade:"))

# Solicita ao usuário que indique se possui dívidas com agiotas, como "Sim" ou "Não".
dividas = input("Você possui dívidas com agiotas? (Sim ou Não):")

# Imprime o salário formatado com duas casas decimais.
print("Seu salário é: R$%.2f" % salario)

# Imprime o nome inserido pelo usuário.
print("Seu nome é:", nome)

# Imprime a idade inserida pelo usuário.
print("Sua idade é:", idade)

# Converte a resposta para minúsculas para tornar a comparação insensível a maiúsculas/minúsculas.
dividas = dividas.lower()

# Verifica se o usuário tem dívidas e responde com um aviso correspondente.
if dividas == "sim":
    print("Tome cuidado.")
elif dividas == "não":
    print("Então tá bom.")
elif dividas == "tenho":
    print("Cuidado ein.")
else:
    print("Cagou no pau. Só existem 'sim', 'tenho' ou 'não' como opções válidas.")

print("Sua idade é:", idade)

# Convertendo a resposta para minúsculas para tornar a comparação não sensível a maiúsculas/minúsculas
dividas = dividas.lower()
if dividas == "sim":
    print("Cuidado cuzão.")

elif dividas == "não":
    print("então ta bom.")
elif dividas == "tenho":
    print("cuidado ein")
else:
    print("Você é muito desatento . só existe 'sim', 'tenho' ou 'não'.")
