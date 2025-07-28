 #5. remove elementos duplicados de uma lista fornecida pelo usuário.
 
ista = []

while True:
    entrada = input("Digite um número (ou 'sair' para terminar): ").strip()

    if entrada.lower() == 'sair':
        break

    try:
        numero = int(entrada)
        # Só adiciona se não existir (mantém ordem)
        if numero not in lista:
            lista.append(numero)
            print(f"Número {numero} adicionado.")
        else:
            print(f"Número {numero} já existe na lista.")

        print(f"Lista atual: {lista}")

    except ValueError:
        print("Por favor, digite um número válido ou 'sair'!")

# Resultado final
print("Lista final sem duplicatas (ordem preservada):")
for numero in lista:
    print(numero)