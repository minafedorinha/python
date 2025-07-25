#Jogo "Adivinhe o Número" onde o computador escolhe um número aleatório e o usuário tenta adivinhar. O programa deve dar dicas se o palpite é maior ou menor que o número escolhido.

import random
numero_secreto = random.randint(1, 100)


contador_tentativas = 0   #esse contador serve para armazenar a quantidade de tentativas tanto para limitar quanto cita-las no acerto

while True:
       try:
          tentativas = 0
          tentativas = int(input("Dê um palpite: "))
          contador_tentativas += 1

          if contador_tentativas >= 10:
           print(f"\nGAME OVER! Você usou todas as 10 tentativas. O número era {numero_secreto}.")
           break

          if tentativas == numero_secreto:
             print(f"Você acertou o número secreto em {tentativas} em {contador_tentativas} tentativas!")
             break
          else :
             if tentativas > numero_secreto and tentativas <= 101:
               print("Errou! Escolha um numero MENOR!")
             elif tentativas < numero_secreto and tentativas <= 101:
               print("Escolha um número MAIOR !")
             elif tentativas < 1 or tentativas > 100:
                print("Por favor, digite um número entre 1 e 100!")

       except ValueError:
              print("Digite números válidos!")       #except serve para rejeitar outro tipo de dado diferente de int, nesse caso
