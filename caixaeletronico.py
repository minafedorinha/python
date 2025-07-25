#Simula um caixa eletrônico, permitindo saques apenas em notas de 100, 50, 20 e 10 reais.
#O programa deve informar a quantidade de cada nota para um determinado valor de saque.
def caixa_eletronico():
    print("Bem-vindo ao Caixa Eletrônico")
    print("Notas disponíveis: R$100, R$50, R$20 e R$10\n")

    while True:
        try:
            valor = int(input("Digite o valor do saque (múltiplo de 10): R$ "))

            if valor <= 0:
                print("Valor inválido! Digite um valor positivo.")
                continue

            if valor % 10 != 0:
                print("Valor inválido! O caixa só trabalha com notas de R$100, R$50, R$20 e R$10.")
                continue

            notas_100 = valor // 100 #Começa pelas maiores notas e vai reduzindo.Usa divisão inteira (//) para contar as notas.Usa módulo (%) para pegar o resto após cada cálculo
            resto = valor % 100

            notas_50 = resto // 50
            resto = resto % 50

            notas_20 = resto // 20
            resto = resto % 20

            notas_10 = resto // 10

            print("\nNotas fornecidas:")
            if notas_100 > 0:
                print(f"{notas_100} nota(s) de R$100")
            if notas_50 > 0:
                print(f"{notas_50} nota(s) de R$50")
            if notas_20 > 0:
                print(f"{notas_20} nota(s) de R$20")
            if notas_10 > 0:
                print(f"{notas_10} nota(s) de R$10")

            print("Deseja realizar outro saque?")
            continuar = input("Digite 'S' para sim ou qualquer tecla para sair: ").upper()
            if continuar != 'S':
                print("Obrigado por utilizar nosso caixa eletrônico!")
                break

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

caixa_eletronico()