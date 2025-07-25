#Gerador de senha onde:
#Tamanho: Mínimo de 8 caracteres.

#Maiúscula: Pelo menos 1 letra (A-Z).

#Minúscula: Pelo menos 1 letra (a-z).

#Número: Pelo menos 1 dígito (0-9).

#Caractere especial: Pelo menos 1 símbolo (ex: !@#$%^&*).

senha = input("Digite sua senha: ")
erros = []
especiais = "!@#$%^&*()_-=+{}[]|;:,.<>?/~`"  # Caracteres especiais estendidos

# Verificação básica de critérios
tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False

# Verifica tamanho mínimo
if len(senha) < 8:
    erros.append("✖ Deve ter pelo menos 8 caracteres")

# Verifica cada caractere
for c in senha:               #Variável temporária que armazena cada caractere da string (pode ter qualquer nome: char, letra, etc.).
                             #O comando for c in senha: é um loop (repetição) que percorre cada caractere de uma string (texto) chamada senha
    if c.isupper():
        tem_maiuscula = True
    elif c.islower():
        tem_minuscula = True
    elif c.isdigit():
        tem_numero = True
    elif c in especiais:
        tem_especial = True

# Coleta erros específicos
if not tem_maiuscula:
    erros.append("✖ Deve conter pelo menos 1 letra maiúscula (A-Z)")
if not tem_minuscula:
    erros.append("✖ Deve conter pelo menos 1 letra minúscula (a-z)")
if not tem_numero:
    erros.append("✖ Deve conter pelo menos 1 número (0-9)")
if not tem_especial:
    erros.append(f"✖ Deve conter pelo menos 1 caractere especial ({especiais})")

# Saída do resultado
if not erros:
    print("\n✅ Senha válida!")

    # Calcula força da senha
    comprimento = len(senha)
    qtd_especiais = sum(1 for c in senha if c in especiais)
    criterios = [tem_maiuscula, tem_minuscula, tem_numero, tem_especial]

    if comprimento >= 12 and qtd_especiais >= 2 and all(criterios):
        forca = "FORTE"
    elif comprimento >= 10 or qtd_especiais >= 1:
        forca = "MÉDIA"
    else:
        forca = "FRACA"

    print(f"""🔒 Análise de segurança:
    - Caracteres: {comprimento}
    - Especiais: {qtd_especiais}
    - Nível de segurança: {forca}""")

else:
    print("❌ Senha inválida. Problemas encontrados:")
    for erro in erros:
        print(f"    {erro}")
    print("Dica: Use uma combinação de diferentes tipos de caracteres!")