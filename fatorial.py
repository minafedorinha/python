#usando o range
def calcular_fatorial(numero):
    fatorial = 1  #Ela é inicializada com 1 porque o fatorial de 0 é 1.
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número positivo para calcular o fatorial: "))
if numero < 0:
    print("Número inválido! Apenas números positivos são aceitos.")
else:
    print(f"O fatorial de {numero} é {calcular_fatorial(numero)}.")