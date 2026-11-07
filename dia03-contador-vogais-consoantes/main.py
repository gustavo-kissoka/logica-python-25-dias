

def contar_vogais(texto):
    vogais = ["a", "e", "i", "o", "u"]
    quantidade = 0
    for letra in texto:
        if letra in vogais:
            quantidade += 1
    return quantidade


def contar_consoantes(texto):
    vogais = ["a", "e", "i", "o", "u"]
    quantidade = 0
    for letra in texto:
        if letra.isalpha():
            if letra not in vogais:
                quantidade += 1
    return quantidade


def contar_numeros(texto):

    quantidade = 0
    for numero in texto:
        if numero.isdigit():
            quantidade += 1

    return quantidade


def contar_espaco(texto):
    quantidade = 0
    for espaco in texto:
        if espaco.isspace():
            quantidade += 1

    return quantidade


def contar_outros(texto):
    outros = 0
    for i in texto:
        if i.isdigit():
            pass
        elif i.isalpha():
            pass
        elif i.isspace():
            pass
        else:
            outros += 1

    return outros


# main
teste = "aaa 342 222 bbb @@@".lower()

# chamada de funções
print(f"Na frase {teste} possui: ")
print("Vogais: ", contar_vogais(teste))
print("Consoantes: ", contar_consoantes(teste))
print("Números: ", contar_numeros(teste))
print("Espaços: ", contar_espaco(teste))
print("Outros: ", contar_outros(teste))
