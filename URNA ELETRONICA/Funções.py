def titulo1 (x):
    soma = 0
    lista = [2, 3, 4, 5, 6, 7, 8, 9]
    for i in range (len(lista)):
        soma += x[i] * lista[i]
    verificação = soma % 11
    if verificação == 10:
        verificação = 0
    if verificação == x[10]:
        return 0
    else:
        return 1


def titulo2 (x):
    soma = 0 
    value = 7
    for i in range (8,11):
        soma += x[i] * value
        value += 1
    verificação = soma % 11
    if verificação == 10:
        verificação = 0
    if verificação == x[11]:
        return 0
    else:
        return 1
    

def votouemquem (x):
    if x == 45:
        aux = '45 - Carlos Paiva (PTC)'
    elif x == 13:
        aux = '13 - Monteiro Lobato (PT)'
    elif x == 12:
        aux = '12 - Elis Regina (PDT)'
    else:
        aux = ' '
    return aux


def apuração (x):
    carlos_paiva = 0
    monteiro_lobato = 0
    elis_regina = 0
    nulos = 0
    brancos = 0
    for i in range(len(x)):
        if x[i] == 45:
            carlos_paiva += 1
        elif x[i] == 13:
            monteiro_lobato += 1
        elif x[i] == 12:
            elis_regina += 1
        elif x[i] == 1001:
            brancos += 1
        else:
            nulos += 1
    if carlos_paiva > monteiro_lobato and carlos_paiva > elis_regina:
        if monteiro_lobato > elis_regina:
            print(f"Carlos Paiva (PTC) - {carlos_paiva} Votos\nMonteiro Lobato (PT) - {monteiro_lobato} Votos\n12 - Elis Regina (PDT) {elis_regina} Votos")
        else:
            print(f"Carlos Paiva (PTC) - {carlos_paiva} Votos\n12 - Elis Regina (PDT) {elis_regina} Votos\nMonteiro Lobato (PT) - {monteiro_lobato} Votos")
    elif monteiro_lobato > carlos_paiva and monteiro_lobato > elis_regina:
        if carlos_paiva > elis_regina:
            print(f"Monteiro Lobato (PT) - {monteiro_lobato} Votos\nCarlos Paiva (PTC) - {carlos_paiva} Votos\n12 - Elis Regina (PDT) {elis_regina} Votos")
        else:
            print(f"Monteiro Lobato (PT) - {monteiro_lobato} Votos\n12 - Elis Regina (PDT) {elis_regina} Votos\nCarlos Paiva (PTC) - {carlos_paiva} Votos")
    elif elis_regina > carlos_paiva and elis_regina > monteiro_lobato:
        if carlos_paiva > monteiro_lobato:
            print(f"12 - Elis Regina (PDT) {elis_regina} Votos\nCarlos Paiva (PTC) - {carlos_paiva} Votos\nMonteiro Lobato (PT) - {monteiro_lobato} Votos")
        else:
            print(f"12 - Elis Regina (PDT) {elis_regina} Votos\nMonteiro Lobato (PT) - {monteiro_lobato} Votos\nCarlos Paiva (PTC) - {carlos_paiva} Votos")
    verificador =  (carlos_paiva + monteiro_lobato + elis_regina)
    porcentagem = verificador * (50/100)
    if carlos_paiva > porcentagem:
        print("Carlos Paiva (PTC)\nFoi Vencedor da eleição")
    elif elis_regina > porcentagem:
        print("Elis Regina (PDT)\nFoi Vencedor da eleição")
    elif monteiro_lobato > porcentagem:
        print("Monteiro Lobato (PT)\nFoi Vencedor da eleição")
    else:
        print("Disputa foi para o segundo turno")