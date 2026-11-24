
"""
Dia 06 - Palíndromo
Cria um programa que diz se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para a frente), ignorando espaços e maiúsculas/minúsculas.
Exemplos: "arara", "Socorram-me subi no onibus em Marrocos" (sem hífen e sem acentos) e "A base do teu amor mamou no bolo".


"""


def palindromo(texto):
    texto_limpo = ""
    texto_reverso = ""

    for letra in texto:
        if letra.isalpha():
            texto_limpo += letra

    for letra in texto_limpo:
        texto_reverso = letra + texto_reverso

    if texto_reverso.lower() == texto_limpo.lower():
        return True
    return False


texto = "A base do teto desaba"
print(palindromo(texto))


# teste
# texto_reverso = texto[::-1]
# print(texto_reverso)
# print(palindromo(texto))
