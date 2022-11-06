import funcoes
from basedequestoes import quest
#inicio do codigo!!!!!
dic_questoes = funcoes.transforma_base(quest)
lista_questoes_sorteadas=[]



print('Olá! Você está jogando Fortuna DesSoft e terá a oportunidade de enriquecer!')
nome=str(input('Qual é seu nome?'))

quer_reiniciar='S'
while quer_reiniciar=='S':
    print(f'OK {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    #enter=str(input('Aperte ENTER para continuar...'))
    print('O jogo já vai começar! Lá vem a primeira questão! ')

    print('Vamos começar com questões do nível FACIL!')
    #enter1=srt(input('Aperte ENTER para continuar...'))
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
                print('Opção inválida!')
                print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
                resp=str(input('Qual sua resposta?!'))

            #parte ajuda feito!! (pequenos retoques futuros!)
            if resp=='ajuda':
                while resp=='ajuda':
                    if ja_pediu_ajuda==1:
                        print('Não deu! Você já pediu ajuda nesta questão!')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==2:
                        print('Não deu! Você não tem mais direito a ajudas!')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==1:
                        ajuda+=1
                        print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==0:
                        ajuda+=1
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    ja_pediu_ajuda=1
            #mudei de elif pra if
            if resp=='pula':
                if pula==3:
                    print('Não deu! Você não tem mais direito a pulos!')

                    while resp=='pula':
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                        if resp=='pula':
                            print('Não deu! Você não tem mais direito a pulos!')
                    break
                elif pula==2:
                    pula+=1
                    print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
                    break
                elif pula==1:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 1 pulo!')
                    break
                elif pula==0:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 2 pulos!')
                    break

            elif resp=='parar':
                deseja_parar=str(input('Deseja mesmo parar [S/N]??'))
                if deseja_parar=='S':
                    decidiu_parar=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'Ok! Você parou e seu prêmio é de R$ {valor}.00')
                    break
            
            if resp in ['A','B','C','D']:
                break
        if resp=='parar':
            break

        if resp in ['A','B','C','D']:
            if resp==alternativa_correta:
                if acertou_quantas_vezes==8:
                    acertou_quantas_vezes+=1
                    print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais!')
                    decidiu_parar=1
                    break
                else:
                    acertou_quantas_vezes+=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'Você acertou! Seu prêmio atual é de R$ {valor}.00')

            elif resp!=alternativa_correta:
                print('Que pena! Você errou e vai sair sem nada :(')
                decidiu_parar=1
                break



    #jogos medios
    if decidiu_parar==0:
        print('HEY! Você passou para o nível MEDIO!')

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
            resp=str(input('Qual sua resposta?!'))

            while resp not in lista_opcoes:
                print('Opção inválida!')
                print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
                resp=str(input('Qual sua resposta?!'))

            #parte ajuda feito!! (pequenos retoques futuros!)
            if resp=='ajuda':
                while resp=='ajuda':
                    if ja_pediu_ajuda==1:
                        print('Não deu! Você já pediu ajuda nesta questão!')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==2:
                        print('Não deu! Você não tem mais direito a ajudas!')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==1:
                        ajuda+=1
                        print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==0:
                        ajuda+=1
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    ja_pediu_ajuda=1

            if resp=='pula':
                if pula==3:
                    print('Não deu! Você não tem mais direito a pulos!')

                    while resp=='pula':
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                        if resp=='pula':
                            print('Não deu! Você não tem mais direito a pulos!')
                    break
                elif pula==2:
                    pula+=1
                    print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
                    break
                elif pula==1:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 1 pulo!')
                    break
                elif pula==0:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 2 pulos!')
                    break

            elif resp=='parar':
                deseja_parar=str(input('Deseja mesmo parar [S/N]??'))
                if deseja_parar=='S':
                    decidiu_parar=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'Ok! Você parou e seu prêmio é de R$ {valor}.00')
                    break

            if resp in ['A','B','C','D']:
                break

        if resp=='parar':
            break

        if resp in ['A','B','C','D']:
            if resp==alternativa_correta:
                if acertou_quantas_vezes==8:
                    acertou_quantas_vezes+=1
                    print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais!')
                    decidiu_parar=1
                    break
                else:
                    acertou_quantas_vezes+=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'Você acertou! Seu prêmio atual é de R$ {valor}.00')

            elif resp!=alternativa_correta:
                print('Que pena! Você errou e vai sair sem nada :(')
                decidiu_parar=1
                break


    #jogos dificeis
    if decidiu_parar==0:
        print('HEY! Você passou para o nível DIFICIL!')

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
            resp=str(input('Qual sua resposta?!'))

            while resp not in lista_opcoes:
                print('Opção inválida!')
                print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
                resp=str(input('Qual sua resposta?!'))

            #parte ajuda feito!! (pequenos retoques futuros!)
            if resp=='ajuda':
                while resp=='ajuda':
                    if ja_pediu_ajuda==1:
                        print('Não deu! Você já pediu ajuda nesta questão!')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==2:
                        print('Não deu! Você não tem mais direito a ajudas!')
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==1:
                        ajuda+=1
                        print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    elif ajuda==0:
                        ajuda+=1
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
                        print(texto_ajuda)
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                    ja_pediu_ajuda=1

            if resp=='pula':
                if pula==3:
                    print('Não deu! Você não tem mais direito a pulos!')

                    while resp=='pula':
                        print(texto_questao)
                        resp=str(input('Qual sua resposta?!'))
                        if resp=='pula':
                            print('Não deu! Você não tem mais direito a pulos!')
                    break
                elif pula==2:
                    pula+=1
                    print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
                    break
                elif pula==1:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 1 pulo!')
                    break
                elif pula==0:
                    pula+=1
                    print('Ok, pulando! Você ainda tem 2 pulos!')
                    break

            elif resp=='parar':
                deseja_parar=str(input('Deseja mesmo parar [S/N]??'))
                if deseja_parar=='S':
                    decidiu_parar=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'Ok! Você parou e seu prêmio é de R$ {valor}.00')
                    break

            if resp in ['A','B','C','D']:
                break

        if resp=='parar':
            break

        if resp in ['A','B','C','D']:
            if resp==alternativa_correta:
                if acertou_quantas_vezes==8:
                    acertou_quantas_vezes+=1
                    print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais!')
                    decidiu_parar=1
                    break
                else:
                    acertou_quantas_vezes+=1
                    valor=lista_valores[acertou_quantas_vezes]
                    print(f'Você acertou! Seu prêmio atual é de R$ {valor}.00')

            elif resp!=alternativa_correta:
                print('Que pena! Você errou e vai sair sem nada :(')
                decidiu_parar=1
                break

    quer_reiniciar=str(input('Deseja reiniciar o jogo?! [S/N] '))







