
def requisitos():
    print("=============VALIDADOR DE PALAVRA-PASSE===========")
    print("Requisitos: ")
    print("Pelo menos 8 caracteres.")
    print("Pelo menor uma letra maiúscula e uma minúscula")
    print("Pelo menos um número.")
    print("Pelo menos um caractere especial (!, @, #, $, %, etc.)")
    print(end="\n")


def validar(palavra_passe):

    maiusculas = 0
    numero = 0
    minuscula = 0
    espaco = 0
    outros = 0

    for caractere in palavra_passe:
        if caractere.isupper():
            maiusculas += 1
        elif caractere.islower():
            minuscula += 1
        elif caractere.isdigit():
            numero += 1
        elif caractere.isspace():
            espaco += 1
        else:
            outros += 1

    if maiusculas == 0:
        print("Falta maiúscula")

    if minuscula == 0:
        print("Falta minúscula")

    if numero == 0:
        print("Falta número")

    if outros == 0:
        print("Falta pelo menos um caractere especial.")

    if len(palavra_passe) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")

    if espaco >= 1:
        print("Não pode ter espaço")

    if (minuscula >= 1 and maiusculas >= 1) and (numero >= 1 and outros >= 1) and (espaco == 0 and len(palavra_passe) >= 8):
        print("Senha válida")
    else:
        print("Senha invalida")


# chamando as funções
requisitos()
validar(palavra_passe="Python123@")
