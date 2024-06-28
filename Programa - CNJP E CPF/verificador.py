def cpf1 (x): #Validação do primeiro dígito do cpf
    soma = 0
    y = 10
    for i in range(9):
        while y > 1:
            soma += x[i] * y
            y -= 1
            break
    verificação = (soma * 10) % 11
    if verificação == 10:
        verificação = 0
    if verificação == x[9]:
        return 0
    else:
        return 1


def cpf2 (x): #Validação do segundo dígito do cpf
    soma = 0
    y = 11
    for i in range(10):
        while y > 1:
            soma += x[i] * y
            y -= 1
            break
    verificação = (soma * 10) % 11
    if verificação == 10:
        verificação = 0
    if verificação == x[10]:
        return 0
    else:
        return 1


def cnpj1 (x): #Validação do primeiro digito do cnpj
    soma = 0
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(12):
        soma += x[i] * pesos[i]
    verificação = soma % 11
    if verificação < 2:
        verificação = 0
    verificação = 11 - verificação
    if verificação == x[12]:
        return 0
    else:
        return 1
    

def cnpj2 (x): #Validação do segundo digito do cnpj
    soma = 0
    pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(13):
        soma += x[i] * pesos[i]
    verificação = (soma % 11)
    if verificação < 2:
        verificação = 0
    verificação = 11 - verificação
    if verificação == x[13]:
        return 0
    else:
        return 1
