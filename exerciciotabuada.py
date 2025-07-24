#Um programa que imprime a tabuada de um número fornecido pelo usuário.

while True:
 try:
     num1 = float(input("Digite o primeiro número da equação: "))
     num2 = float(input("Digite o segundo número da equação: "))
     operacao = input(" +, -, %, x : ")


     if operacao == "+":
        result = num1 + num2
        print("O resultado é:", result)

     elif operacao == "-":
        result = num1 - num2
        print("O resultado é:", result)

     elif operacao == "%":
        result = num1 % num2
        print("O resultado é:", result)

     elif operacao == "x":
        result = num1 * num2
        print("O resultado é:", result)


     else:
      print("Operação inválida!")

 except ValueError:
        print("Digite números válidos!")

 continuar = input("Deseja fazer outro cálculo? (s/n): ").lower() #converte a resposta para minúsculo (para aceitar 'S' ou 's')
 if continuar != "s":
  print("Encerrando a calculadora...")
  break

