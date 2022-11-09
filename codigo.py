import funcoes
from basedequestoes import quest
#inicio do codigo!!!!!
dic_questoes = funcoes.transforma_base(quest)
lista_questoes_sorteadas=[]

#validando a base de dados!



print('\033[32mOlá! Você está jogando Fortuna DesSoft e terá a oportunidade de enriquecer!\033[m\n')
nome=str(input('Qual é seu nome?\n'))

quer_reiniciar='S'
while quer_reiniciar=='S':
    print(f'OK {nome}, você tem direito a pular 3 vezes e 2 ajudas!\n')
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
    enter=input('Aperte ENTER para continuar...\n')
    print('O jogo já vai começar! Lá vem a primeira questão! \n')

    print('\033[32mVamos começar com questões do nível FACIL!\033[m\n')
    enter1=input('Aperte ENTER para continuar...\n')
    pula=0
    ajuda=0

    id_questao=0
    facil=0
    medio=0
    dificil=0

    acertou_quantas_vezes=0
    lista_valores=[0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]

    lista_opcoes=['A','B','C','D','ajuda','pula','parar']

    for nivel,lista in dic_questoes.items():
        if nivel=='facil':
            tot_facil=len(lista)
        elif nivel=='medio':
            tot_medio=len(lista)
        elif nivel=='dificil':
            tot_dificil=len(lista)

    decidiu_parar=0


    #jogos faceis

    while True:
        ja_pediu_ajuda=0

        facil+=1
        if acertou_quantas_vezes>3:
            break
        if decidiu_parar!=0:
            decidiu_parar=1
            break
        id_questao+=1
        #nivelfácil
        
        questao_sorteada=funcoes.sorteia_questao_inedida(dic_questoes,'facil',lista_questoes_sorteadas)
        alternativa_correta=questao_sorteada['correta']
        lista_questoes_sorteadas.append(questao_sorteada)
        texto_questao=funcoes.questao_para_texto(questao_sorteada,id_questao)
        texto_ajuda=funcoes.gera_ajuda(questao_sorteada)

        while True:
            print(texto_questao)
            resp=str(input('Qual sua resposta?!'))

            while resp not in lista_opcoes:
                print('\033[31mOpção inválida!\033[m\n')
                print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
                resp=str(input('Qual sua resposta?!\n'))

            #parte ajuda feito!! (pequenos retoques futuros!)
            if resp=='ajuda':
                while resp=='ajuda':
                    if ja_pediu_ajuda==1:
                        print('\033[31mNão deu! Você já pediu ajuda nesta questão!\033[m\n')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==2:
                        print('\033[31mNão deu! Você não tem mais direito a ajudas!\033[m\n')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==1:
                        ajuda+=1
                        print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!\n')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==0:
                        ajuda+=1
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!\n')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    ja_pediu_ajuda=1
            #mudei de elif pra if
            if resp=='pula':
                if pula==3:
                    print('\033[31mNão deu! Você não tem mais direito a pulos!\033[m\n')

                    while resp=='pula':
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                        if resp=='pula':
                            print('\033[31mNão deu! Você não tem mais direito a pulos!\033[m\n')
                    break
                elif pula==2:
                    pula+=1
                    print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!\n')
                    break
                elif pula==1:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 1 pulo!\n')
                    break
                elif pula==0:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 2 pulos!\n')
                    break

            elif resp=='parar':
                deseja_parar=str(input('\033[31mDeseja mesmo parar [S/N]??\033[m\n'))
                if deseja_parar=='S':
                    decidiu_parar=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'\033[32mOk! Você parou e seu prêmio é de R$ {valor}.00\033[m\n')
                    break
            
            if resp in ['A','B','C','D']:
                break
        if resp=='parar':
            break

        if resp in ['A','B','C','D']:
            if resp==alternativa_correta:
                if acertou_quantas_vezes==8:
                    acertou_quantas_vezes+=1
                    print('\033[32mPARABÉNS, você zerou o jogo e ganhou um milhão de reais!\033[m\n')
                    decidiu_parar=1
                    break
                else:
                    acertou_quantas_vezes+=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'\033[32mVocê acertou! Seu prêmio atual é de R$ {valor}.00\033[m\n')

            elif resp!=alternativa_correta:
                print('\033[31mQue pena! Você errou e vai sair sem nada :(\033[m\n')
                decidiu_parar=1
                break



    #jogos medios
    if decidiu_parar==0:
        print('\033[32mHEY! Você passou para o nível MEDIO!\033[m\n')

    while True:
        ja_pediu_ajuda=0

        medio+=1
        if acertou_quantas_vezes>6:
            break
        if decidiu_parar!=0:
            decidiu_parar=1
            break
        id_questao+=1
        #nivelmedio
        
        questao_sorteada=funcoes.sorteia_questao_inedida(dic_questoes,'medio',lista_questoes_sorteadas)
        alternativa_correta=questao_sorteada['correta']
        lista_questoes_sorteadas.append(questao_sorteada)
        texto_questao=funcoes.questao_para_texto(questao_sorteada,id_questao)
        texto_ajuda=funcoes.gera_ajuda(questao_sorteada)

        while True:
            print(texto_questao)
            resp=str(input('Qual sua resposta?!\n'))

            while resp not in lista_opcoes:
                print('\033[31mOpção inválida!\033[m\n')
                print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
                resp=str(input('Qual sua resposta?!\n'))

            #parte ajuda feito!! (pequenos retoques futuros!)
            if resp=='ajuda':
                while resp=='ajuda':
                    if ja_pediu_ajuda==1:
                        print('\033[31mNão deu! Você já pediu ajuda nesta questão!\033[m\n')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==2:
                        print('\033[31mNão deu! Você não tem mais direito a ajudas!\033[m\n')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==1:
                        ajuda+=1
                        print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!\n')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==0:
                        ajuda+=1
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!\n')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    ja_pediu_ajuda=1

            if resp=='pula':
                if pula==3:
                    print('\033[31mNão deu! Você não tem mais direito a pulos!\033[m\n')

                    while resp=='pula':
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                        if resp=='pula':
                            print('\033[31mNão deu! Você não tem mais direito a pulos!\033[m\n')
                    break
                elif pula==2:
                    pula+=1
                    print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!\n')
                    break
                elif pula==1:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 1 pulo!\n')
                    break
                elif pula==0:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 2 pulos!\n')
                    break

            elif resp=='parar':
                deseja_parar=str(input('Deseja mesmo parar [S/N]??\n'))
                if deseja_parar=='S':
                    decidiu_parar=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'\033[32mOk! Você parou e seu prêmio é de R$ {valor}.00\033[m\n')
                    break

            if resp in ['A','B','C','D']:
                break

        if resp=='parar':
            break

        if resp in ['A','B','C','D']:
            if resp==alternativa_correta:
                if acertou_quantas_vezes==8:
                    acertou_quantas_vezes+=1
                    print('\033[32mPARABÉNS, você zerou o jogo e ganhou um milhão de reais!\033[m\n')
                    decidiu_parar=1
                    break
                else:
                    acertou_quantas_vezes+=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'\033[32mVocê acertou! Seu prêmio atual é de R$ {valor}.00\033[m\n')

            elif resp!=alternativa_correta:
                print('\033[31mQue pena! Você errou e vai sair sem nada :(\033[m\n')
                decidiu_parar=1
                break


    #jogos dificeis
    if decidiu_parar==0:
        print('\033[32mHEY! Você passou para o nível DIFICIL!\033[m\n')

    while True:
        ja_pediu_ajuda=0

        dificil+=1
        if acertou_quantas_vezes>9:
            break
        if decidiu_parar!=0:
            decidiu_parar=1
            break
        id_questao+=1
        #niveldificil
        
        questao_sorteada=funcoes.sorteia_questao_inedida(dic_questoes,'dificil',lista_questoes_sorteadas)
        alternativa_correta=questao_sorteada['correta']
        lista_questoes_sorteadas.append(questao_sorteada)
        texto_questao=funcoes.questao_para_texto(questao_sorteada,id_questao)
        texto_ajuda=funcoes.gera_ajuda(questao_sorteada)

        while True:
            print(texto_questao)
            resp=str(input('Qual sua resposta?!\n'))

            while resp not in lista_opcoes:
                print('\033[31mOpção inválida!\033[m')
                print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
                resp=str(input('Qual sua resposta?!'))

            #parte ajuda feito!! (pequenos retoques futuros!)
            if resp=='ajuda':
                while resp=='ajuda':
                    if ja_pediu_ajuda==1:
                        print('\033[31mNão deu! Você já pediu ajuda nesta questão!\033[m\n')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==2:
                        print('\033[31mNão deu! Você não tem mais direito a ajudas!\033[m\n')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==1:
                        ajuda+=1
                        print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!\n')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    elif ajuda==0:
                        ajuda+=1
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!\n')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!\n'))
                    ja_pediu_ajuda=1

            if resp=='pula':
                if pula==3:
                    print('\033[31mNão deu! Você não tem mais direito a pulos!\033[m\n')

                    while resp=='pula':
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                        if resp=='pula':
                            print('\033[31mNão deu! Você não tem mais direito a pulos!\033[m\n')
                    break
                elif pula==2:
                    pula+=1
                    print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!\n')
                    break
                elif pula==1:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 1 pulo!\n')
                    break
                elif pula==0:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 2 pulos!\n')
                    break

            elif resp=='parar':
                deseja_parar=str(input('Deseja mesmo parar [S/N]??\n'))
                if deseja_parar=='S':
                    decidiu_parar=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'\033[32mOk! Você parou e seu prêmio é de R$ {valor}.00\033[m\n')
                    break

            if resp in ['A','B','C','D']:
                break

        if resp=='parar':
            break

        if resp in ['A','B','C','D']:
            if resp==alternativa_correta:
                if acertou_quantas_vezes==8:
                    acertou_quantas_vezes+=1
                    print('\033[32mPARABÉNS, você zerou o jogo e ganhou um milhão de reais!\033[m\n')
                    decidiu_parar=1
                    break
                else:
                    acertou_quantas_vezes+=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'\033[32mVocê acertou! Seu prêmio atual é de R$ {valor}.00\033[m\n')

            elif resp!=alternativa_correta:
                print('\033[31mQue pena! Você errou e vai sair sem nada :(\033[m\n')
                decidiu_parar=1
                break

    quer_reiniciar=str(input('Deseja reiniciar o jogo?! [S/N] \n'))







