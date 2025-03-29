import random
print ("---- Elevador / Prédio ----")
escolha = int(input("1 - Andar (Térreo)\n2 - Andar (1)\n3 - Andar (2)\n4 - Andar (3)\nEscolha: "))
elevador = random.randint(1,4)
while True: 
    if escolha == 1: #TERREO
        if elevador != 1:
            print (f"Elevador em outro andar!\nChamando Elevador...\n...Elevador no Andar: {"Térreo"}")
        else:
            print ("Térreo - Andar 0")
        escolha_terreo = str(input("Entrar ou Sair? ")).capitalize()
        if escolha_terreo == "Entrar": 
            print ("Entrando...")
            andar_terreo = int(input("Qual andar deseja ir? "))
            print (f"Indo ao andar desejado, Andar: {andar_terreo}")
            while True:
                novamente_terreo = str(input("Deseja acessar o elevador novamente (s/n)? ")).lower()
                if novamente_terreo == "s":
                    while True:
                        nov = int(input("Qual andar deseja ir? "))
                        if nov >= 5:
                            print ("Digite um andar válido!")
                        else:
                            print (f"Indo ao andar desejado, Andar: {nov}")
                            break
                else:
                    print (f"Ok, Andar: {andar_terreo}")
                elevador += andar_terreo or novamente_terreo
                break
            break
        elif escolha_terreo == "Sair":
            print ("Saindo... Térreo")
            while True:
                novamente_terreo = str(input("Deseja acessar o elevador novamente (s/n)? ")).lower()
                if novamente_terreo == "s":
                    while True:
                        nov = int(input("Qual andar deseja ir? "))
                        if nov >= 5:
                            print ("Digite um andar válido!")
                        else:
                            print (f"Indo ao andar desejado, Andar: {nov}")
                            break
                else:
                    print (f"Ok, Andar: {andar_terreo}")
        if novamente_terreo == "s":
            elevador += nov
        elif novamente_terreo == "n":
            elevador += andar_terreo
            break   
        break
    if escolha == 2: #PRIMEIRO ANDAR
        if elevador != 2:
            print (f"Elevador em outro andar!\nChamando Elevador...\n...Elevador no Andar: {"Primeiro Andar"}")
        else:
            print ("Primeiro Andar - 1")
        escolha_primeiro = str(input("Entrar ou Sair? ")).capitalize()
        if escolha_primeiro == "Entrar": 
            print ("Entrando...")
            andar_primeiro = int(input("Qual andar deseja ir? "))
            print (f"Indo ao andar desejado, Andar: {andar_primeiro}")
            while True:
                novamente_primeiro = str(input("Deseja acessar o elevador novamente (s/n)? ")).lower()
                if novamente_primeiro == "s":
                    while True:
                        nov_primeiro = int(input("Qual andar deseja ir? "))
                        if nov_primeiro >= 5:
                            print ("Digite um andar válido!")
                        else:
                            print (f"Indo ao andar desejado, Andar: {nov_primeiro}")
                            break
                else:
                    print (f"Ok, Andar: {andar_primeiro}")
                elevador += andar_primeiro or novamente_primeiro
                break
            break
        elif escolha_primeiro == "Sair":
            print ("Saindo... Térreo")
            while True:
                novamente_primeiro = str(input("Deseja acessar o elevador novamente (s/n)? ")).lower()
                if novamente_primeiro == "s":
                    while True:
                        nov_primeiro = int(input("Qual andar deseja ir? "))
                        if nov_primeiro >= 5:
                            print ("Digite um andar válido!")
                        else:
                            print (f"Indo ao andar desejado, Andar: {nov_primeiro}")
                            break
                else:
                    print (f"Ok, Andar: {andar_primeiro}")
        if novamente_primeiro == "s":
            elevador += nov
        elif novamente_primeiro == "n":
            elevador += andar_primeiro
            break   
        break
    if escolha == 3: #SEGUNDO ANDAR
        if elevador != 3:
            print (f"Elevador em outro andar!\nChamando Elevador...\n...Elevador no Andar: {"Segundo Andar"}")
        else:
            print ("Segundo Andar - 2")
        escolha_seg = str(input("Entrar ou Sair? ")).capitalize()
        if escolha_seg == "Entrar": 
            print ("Entrando...")
            andar_seg = int(input("Qual andar deseja ir? "))
            print (f"Indo ao andar desejado, Andar: {andar_seg}")
            while True:
                novamente_seg = str(input("Deseja acessar o elevador novamente (s/n)? ")).lower()
                if novamente_seg == "s":
                    while True:
                        nov_seg = int(input("Qual andar deseja ir? "))
                        if nov_seg >= 5:
                            print ("Digite um andar válido!")
                        else:
                            print (f"Indo ao andar desejado, Andar: {nov_seg}")
                            break
                else:
                    print (f"Ok, Andar: {andar_seg}")
                elevador += andar_seg or novamente_seg
                break
            break
        elif escolha_seg == "Sair":
            print ("Saindo... Segundo Andar")
            while True:
                novamente_seg = str(input("Deseja acessar o elevador novamente (s/n)? ")).lower()
                if novamente_seg == "s":
                    while True:
                        nov_seg = int(input("Qual andar deseja ir? "))
                        if nov_seg >= 5:
                            print ("Digite um andar válido!")
                        else:
                            print (f"Indo ao andar desejado, Andar: {nov_seg}")
                            break
                else:
                    print (f"Ok, Andar: {andar_seg}")
        if novamente_seg == "s":
            elevador += nov_seg
        elif novamente_seg == "n":
            elevador += andar_seg
            break   
        break
    if escolha == 4: #TERCEIRO ANDAR
        if elevador != 4:
            print (f"Elevador em outro andar!\nChamando Elevador...\n...Elevador no Andar: {"Terceiro Andar"}")
        else:
            print ("Terceiro Andar - 3")
        escolha_ter = str(input("Entrar ou Sair? ")).capitalize()
        if escolha_ter == "Entrar": 
            print ("Entrando...")
            andar_ter = int(input("Qual andar deseja ir? "))
            print (f"Indo ao andar desejado, Andar: {andar_ter}")
            while True:
                novamente_ter = str(input("Deseja acessar o elevador novamente (s/n)? ")).lower()
                if novamente_ter == "s":
                    while True:
                        nov_ter = int(input("Qual andar deseja ir? "))
                        if nov_ter >= 5:
                            print ("Digite um andar válido!")
                        else:
                            print (f"Indo ao andar desejado, Andar: {nov_ter}")
                            break
                else:
                    print (f"Ok, Andar: {andar_ter}")
                elevador += andar_ter or novamente_ter
                break
            break
        elif escolha_ter == "Sair":
            print ("Saindo... Terceiro Andar")
            while True:
                novamente_ter = str(input("Deseja acessar o elevador novamente (s/n)? ")).lower()
                if novamente_ter == "s":
                    while True:
                        nov_ter = int(input("Qual andar deseja ir? "))
                        if nov_ter >= 5:
                            print ("Digite um andar válido!")
                        else:
                            print (f"Indo ao andar desejado, Andar: {nov_ter}")
                            break
                else:
                    print (f"Ok, Andar: {andar_ter}")
        if novamente_ter == "s":
            elevador += nov_seg
        elif novamente_ter == "n":
            elevador += andar_ter
            break   
        break
    else:
        print ("Selecione um Andar Válido!")
        break;