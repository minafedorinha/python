def multiplicar_por_dois(numero):
    resultado = numero * 2
    return resultado

def somar_tudo(valor1, valor2, valor):
    resultado = valor1 + valor2 + valor
    return resultado

# criei a função multiplicar_por_dois para configurar o bonus do jogador
valor1 = multiplicar_por_dois(10)
print("Seu primeiro bonus é" ,valor1)
valor2 = multiplicar_por_dois(20)
print("Seu segundo bonus é" ,valor2)

valor_do_usuario = int(input("Digite um número: "))
valor = multiplicar_por_dois(valor_do_usuario)
print("Sua moeda equivale a:" ,valor)

total = somar_tudo(valor1, valor2, valor)
print("Seu total de bonus é", total)