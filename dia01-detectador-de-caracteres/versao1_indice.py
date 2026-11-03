palavra = input("Digite qualquer palavra que contenha(números, caracteres especiais pode ter espaço): ")

# ccontadores da entrada 
letra = 0
numero = 0
espaco = 0
caractere_especial = 0

for i in range(len(palavra)):
    if palavra[i].isalpha():
        letra += 1
    elif palavra[i].isdigit():
        numero += 1
    elif palavra[i].isspace():
        espaco += 1
    else:
        caractere_especial += 1   


# print dos resultados 
print(f"Letras: {letra}")
print(f"Números: {numero}")
print(f"Espaços: {espaco}")
print(f"Outros: {caractere_especial}")