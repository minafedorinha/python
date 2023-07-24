salario = int(input("Digite seu salario:"))
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
dividas = input("Você possui dívidas com agiotas? (Sim ou Não):")

print("Seu salário é: R$%.2f" % salario)
print("Seu nome é:", nome)
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
    print("Cagou no pau. só existe 'sim', 'tenho' ou 'não'.")
