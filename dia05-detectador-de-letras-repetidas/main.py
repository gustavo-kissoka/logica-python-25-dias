def letras_repetidas(texto):
    letra_mais_repetida = []
    maior_quantidade = 0

    for i in texto:
        contador = 0
        if i in texto:
            for j in texto:
                if j == i:
                    contador += 1
            if contador > maior_quantidade:
                maior_quantidade = contador
                letra_mais_repetida = [i]  # reinicia a lista
            elif contador == maior_quantidade and i not in letra_mais_repetida:
                letra_mais_repetida.append(i)
    print(
        f"Letra(s) que mais repetiram é: {letra_mais_repetida} -> {maior_quantidade} vezes")


letras_repetidas("Mississippi")
letras_repetidas("banana")
