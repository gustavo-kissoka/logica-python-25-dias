def palavra_mais_longa(frase):
    maior_palavra = ""
    palavra_atual = ""

    for carac in frase + " ":
        if carac.isalpha():
            palavra_atual += carac
        else:
            if len(palavra_atual) > len(maior_palavra):
                maior_palavra = palavra_atual
            palavra_atual = ""
    return f"A maior palavra é: {maior_palavra} com {len(maior_palavra)} letras"


frase = "O Gustavo estuda programação"
mensagem = palavra_mais_longa(frase)
print(mensagem)
