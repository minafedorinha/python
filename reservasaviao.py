class Reserva:
    def __init__(self, aviao, passageiro):
        self.aviao = aviao
        self.passageiro = passageiro

def main():
    avioes = [0] * 4
    assentos = [20] * 4
    reservas = []

    while True:
     print('================SEJA BEM VINDO AO SISTEMA DA SWEET FLIGHT==============')
     print("1- REGISTRAR O NUMERO DE CADA AVIÃO")
     print("2- REGISTRAR O QUANTITATIVO DE ASSENTOS EM CADA AVIÃO")
     print("3- RESERVAR PASSAGEM AÉREA")
     print("4- REALIZAR CONSULTA POR AVIÃO")
     print("5- REALIZAR CONSULTA POR PASSAGEIRO")
     print("6- ENCERRAR")

     opcao = input("Escolha a opção desejada: ")

     if opcao == "1":
            print("Registro de Aviões:")
            for i in range(4):
                avioes[i] = input(f"Digite o ID do {i+1}º avião: ")
            print("Aviões registrados com sucesso!")

     elif opcao == "2":
            if avioes[0] == 0:
                print("Primeiro registre os números dos aviões na opção 1!")
                continue

            print("--- Assentos Disponíveis por Avião ---")
            for i in range(4):
                print(f"Avião {avioes[i]}: {assentos[i]} assentos livres (de 20)")

     elif opcao == "3":
            if len(reservas) >= 80:  # 4 aviões * 20 assentos = 80 reservas máximas
                print("O limite de reservas foi atingido!")
                continue

            if avioes[0] == 0:
                print("Primeiro registre os números dos aviões na opção 1!")
                continue

            print("Assentos disponíveis:")
            for i in range(4):
                print(f"Avião {avioes[i]}: {assentos[i]} assentos livres")

            num_aviao = input("Digite o ID do avião para reserva: ")

            if num_aviao not in avioes:
                print("Este avião não existe!")
                continue

            indice_aviao = avioes.index(num_aviao)

            if assentos[indice_aviao] <= 0:
                print("Não há assentos disponíveis para este avião!")
                continue

            nome_passageiro = input("Digite o nome do passageiro: ")

            reservas.append(Reserva(num_aviao, nome_passageiro))
            assentos[indice_aviao] -= 1
            print(f"Reserva realizada com sucesso! Assentos restantes no avião {num_aviao}: {assentos[indice_aviao]}")

     elif opcao == "4":
            if not reservas:
                print("Não há reservas realizadas ainda!")
                continue

            num_aviao = input("Digite o número do avião para consulta: ")

            if num_aviao not in avioes:
                print("Este avião não existe!")
                continue

            reservas_aviao = [r for r in reservas if r.aviao == num_aviao]

            if not reservas_aviao:
                print(f"Não há reservas realizadas para o avião {num_aviao}!")
            else:
                print(f"Reservas para o avião {num_aviao}:")
                for i, reserva in enumerate(reservas_aviao, 1):
                    print(f"{i}. Passageiro: {reserva.passageiro}")

     elif opcao == "5":
            if not reservas:
                print("Não há reservas realizadas ainda!")
                continue

            nome_passageiro = input("Digite o nome do passageiro para consulta: ")

            reservas_passageiro = [r for r in reservas if r.passageiro.lower() == nome_passageiro.lower()]

            if not reservas_passageiro:
                print("Não há reservas realizadas para este passageiro!")
            else:
                print(f"Reservas para o passageiro {nome_passageiro}:")
                for reserva in reservas_passageiro:
                    aviao = reserva.aviao
                    indice = avioes.index(aviao)
                    print(f"Avião {aviao} ")

     elif opcao == "6":
            print("Encerrando o sistema...")
            break

     else:
            print("Opção inválida! Digite um número de 1 a 6.")

if __name__ == "__main__":
    main()