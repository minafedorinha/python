def multiplicar_por_dois(numero):
    resultado = numero * 2
    return resultado

def somar_tudo(recebe_valor1, recebe_valor2, recebe_valor3):
    resultado = recebe_valor1 + recebe_valor2 + recebe_valor3
    return resultado



# criei a função multiplicar_por_dois para
valor1 = multiplicar_por_dois(10)
print("Seu primeiro bonus é", valor1)
valor2 = multiplicar_por_dois(20)
print("Seu segundo bonus é", valor2)

valor_do_usuario = int(input("Digite um número: "))
valor = multiplicar_por_dois(valor_do_usuario)
print("Sua moeda equivale a:", valor)

total = somar_tudo(valor1, valor2, valor)
print("Seu total de bônus é", total)
