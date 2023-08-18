# Tais funções vão tratar, isoladamente, as variáveis abaixo. 
#A função é basicamente um sistema de entrada(recebe) e a saida(devolve) das informações
def calcular_media(recebe_nota1, recebe_nota2):
    return (recebe_nota1 + recebe_nota2) / 2

def ler_nota():
    nota = int(input("Digite sua nota: "))
    return nota

nota1 = ler_nota()
nota2 = ler_nota()
# Na variável acima,convoca-se a função ler_nota para configurar a informção 
# armazenada em um numero inteiro.
media = calcular_media(nota1, nota2)
# o valor armazenado em media vai ser: nota1 e nota2 passando pela função calcular_media.
# na função, a informação entre () é a interface ou parametro. Ela possui o parametro
#pelo fato de que os valores já estao determinados pelo usuário.

print("Sua primeira nota:", nota1)
print("Sua segunda nota:", nota2)
print("Média:", media)

if media >= 7:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado.")
# if >= else é um operador lógico. 7 é o parametro 
