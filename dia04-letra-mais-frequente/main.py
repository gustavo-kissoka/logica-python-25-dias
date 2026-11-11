def letra_mais_frequente(texto):
    maior_quantidade = 0
    letra_vencedora = ""

    for i in texto.lower():
        contador = 0
        for j in texto.lower():
            if j == i:
                contador += 1
        if contador > maior_quantidade:
            maior_quantidade = contador
            letra_vencedora = i
    print(
        f"Letra com mais frequancia: {letra_vencedora} apareceu {maior_quantidade} vezes")


letra_mais_frequente("12345 @@@ !!!")
