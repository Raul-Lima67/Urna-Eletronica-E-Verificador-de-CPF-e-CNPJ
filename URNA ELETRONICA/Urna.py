from Funções import *
start = 0
votos = []
candidato45 = '45 - Carlos Paiva (PTC)'
candidato13 = '13 - Monteiro Lobato (PT)'
candidato12 = '12 - Elis Regina (PDT)'
while start != 2:
    print("")
    print("URNA PY".center(20))
    print(f"ESCOLHA SEU VOTO:\n{candidato45}\n{candidato13}\n{candidato12}")
    start = int(input("1 - Votar       2 - Apurar votos\n"))
    if start == 1:
        title = 1
        while title != 0:
            titulo = input("\nDigite titulo eleitoral do eleitor: ")
            lista = []
            for i in titulo:
                if i == '0' or i == '1' or i == '2' or  i == '3' or  i == '4' or i == '5' or  i == '6' or i == '7' or i == '8' or i == '9':
                    lista.append(int(i))   
            etapa1 = titulo1(lista)
            if etapa1 == 0:
                etapa2 = (titulo2(lista))
                if etapa2 == 0:
                    title = 0
                else:
                    print("Titulo do eleitor invalido!, Tente novamente")
            else:
                print("Titulo do eleitor invalido!, Tente novamente")
        x = int(input("\n1 - Votar em um Candidato       2 - Votar em branco\n"))
        if x == 1:
            votar = int(input("\nInforme o número correspondente ao seu candidato\n"))
            aux = votouemquem(votar)
            y = int(input(f"\nO Candidato é\n{aux} \n1 - Confirmar       2 - Corrigir"))
            if y == 1:
                print(f"\nSeu titulo: {titulo}\nVocê votou no candidato: {aux}")
                votos.append(votar)
            else:
                tentativas = 0
                while y == 2:
                    tentativas += 1
                    if tentativas > 3:
                        print(f"\nSeu titulo: {titulo}\nVocê votou no candidato: {aux}")
                        votos.append(votar)
                        break
                    print(f"\n{tentativas} tentativa!!!\nVocê ainda tem {3 - tentativas} tentativas(s)")
                    votar = int(input("\nInforme o número correspondente ao seu candidato\n"))
                    aux = votouemquem(votar)
                    y = int(input(f"\nSeu voto foi \n{aux}\n1 - Confirmar       2 - Corrigir\n"))
                    if y == 1:
                        print(f"\nSeu titulo: {titulo}\nVocê votou no candidato: {aux}")
                        votos.append(votar)
                        break
        else:
            print(f"\n{titulo}\nVocê votou no candidato: {aux}")
            votos.append(1001)
    elif start == 2:
        x = input("Digite a senha da apuração\n") 
        while x != 'fim':
            print("Senha incorreta!\nTente novamente")
        if x == 'fim':
            apuração(votos)
