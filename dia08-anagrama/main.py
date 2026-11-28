def anagrama(t1, t2):
    t1_limpo = ""
    for c in t1:
        if c.isalpha():
            t1_limpo += c.lower()

    t2_limpo = ""
    for c in t2:
        if c.isalpha():
            t2_limpo += c.lower()

    if len(t1_limpo) != len(t2_limpo):
        print("O tamanho não cumpre.")
        return False
    else:
        # cria uma lista caractere por caractere do segundo texto
        t2_lst = []
        for i in t2_limpo:
            t2_lst.append(i)

        for i in t1_limpo:
            encontrou = False
            for j in range(len(t2_lst)):
                if i == t2_lst[j]:
                    encontrou = True
                    t2_lst[j] = "#"
                    break
            if not encontrou:
                return False
        return True


t1 = "Dormitory!"
t2 = "Dirty room"

print(anagrama(t1, t2))  # True
