palavra = input("Digite qualquer palavra que contenha(números,"
                " caracteres especiais pode ter espaço): ")

# ccontadores da entrada
letra = 0
numero = 0
espaco = 0
outros = 0

for caractere in palavra:
    if caractere.isalpha():
        letra += 1
    elif caractere.isdigit():
        numero += 1
    elif caractere.isspace():
        espaco += 1
    else:
        outros += 1


# print dos resultados
print(f"Letras: {letra}")
print(f"Números: {numero}")
print(f"Espaços: {espaco}")
print(f"Outros: {outros}")
