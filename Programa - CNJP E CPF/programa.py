from verificador import *
q_cpf = 0  #quantativo de cpfs validados
q_cnpj = 0 #quantitativo de cnpj validados
x_cpf = 0 #cpf não validados
x_cnpj = 0 #cnpj não validados
x = 1
while x != 'SAIR':
    print("")
    print("VERIFICAÇÃO PY".center(30))
    x = input("Digite uma opção\n<Sair>    Validar <CNPJ>     Validar <CPF>\n")
    y = x.upper()
    if y == 'SAIR':
        break
    elif y == 'CNPJ':
        cnpj = input("\nDigite seu CNPJ: ")
        lista = []
        for i in cnpj:
            if i == '0' or i == '1' or i == '2' or  i == '3' or  i == '4' or i == '5' or  i == '6' or i == '7' or i == '8' or i == '9':
                lista.append(int(i))
        etapa1 = cnpj1(lista)
        if etapa1 == 0:
            etapa2 = cnpj2(lista)
            if etapa2 == 0:
                print("\nCNPJ válido")
                print(f"{lista[0]}{lista[1]}.{lista[2]}{lista[3]}{lista[4]}.{lista[5]}{lista[6]}{lista[7]}.{lista[8]}{lista[9]}{lista[10]}{lista[11]}-{lista[12]}{lista[13]}")
                q_cnpj += 1
            else:
                print("\nCNPJ inválido, entre em contato com a receita federal")
                x_cnpj += 1
        else:
            print("\nCNPJ inválido, entre em contato com a receita federal")
            x_cnpj += 1
    elif y == 'CPF':
        cpf = input("\nDigite seu CPF: ")
        lista = []
        for i in cpf:
            if i == '0' or i == '1' or i == '2' or  i == '3' or  i == '4' or i == '5' or  i == '6' or i == '7' or i == '8' or i == '9':
                lista.append(int(i))
        etapa1 = cpf1(lista)
        if etapa1 == 0:
            etapa2 = cpf2(lista)
            if etapa2 == 0:
                print("\nCPF válido")
                print(f"{lista[0]}{lista[1]}{lista[2]}.{lista[3]}{lista[4]}{lista[5]}.{lista[6]}{lista[7]}{lista[8]}-{lista[9]}{lista[10]}") 
                q_cpf += 1
            else:
                print("\nCPF inválido, entre em contato com a receita federal")
                x_cpf += 1
        else:
            print("\nCPF inválido, entre em contato com a receita federal")
            x_cpf += 1
print(f"\nForam Validados:\n{q_cpf} CPF's\n{q_cnpj} CNPJ's\n\nForam Invalidados:\n{x_cpf} CPF's\n{x_cnpj} CNPJ's")