import funcoes
from basedequestoes import quest
#inicio do codigo!!!!!
dic_questoes = funcoes.transforma_base(quest)
lista_questoes_sorteadas=[]



print('Olá! Você está jogando Fortuna DesSoft e terá a oportunidade de enriquecer!')
nome=str(input('Qual é seu nome?'))
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

acertou_quantas_vezes=-1
lista_valores=[1000,5000,10000,30000,50000,100000,300000,500000,1000000]

lista_opcoes=['A','B','C','D','ajuda','pula','para']

for nivel,lista in dic_questoes.items():
    if nivel=='facil':
        tot_facil=len(lista)
    elif nivel=='medio':
        tot_medio=len(lista)
    elif nivel=='dificil':
        tot_dificil=len(lista)

decidiu_parar=0


#quantidade de jogos faceis
while True:
    facil+=1
    if facil>tot_facil:
        break
    if decidiu_parar!=0:
        decidiu_parar=1
        break
    id_questao+=1
    #nivelfácil
    questao_sorteada=funcoes.sorteia_questao_inedida(dic_questoes,facil,lista_questoes_sorteadas)
    alternativa_correta=questao_sorteada['correta']
    lista_questoes_sorteadas.append(questao_sorteada)
    texto_questao=funcoes.questao_para_texto(questao_sorteada,id_questao)
    texto_ajuda=funcoes.gera_ajuda(questao_sorteada)
    print(texto_questao)
    resp=str(input('Qual sua resposta?!'))
    while resp not in lista_opcoes:
        print('Opção inválida!')
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
        resp=str(input('Qual sua resposta?!'))
    if resp=='ajuda':
        if ajuda==2:
            print('Não deu! Você não tem mais direito a ajudas!')
        elif ajuda==1:
            ajuda+=1
            print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!')
            print(texto_ajuda)
            resp=str(input('Qual sua resposta?!'))
        elif ajuda==0:
            ajuda+=1
            print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
            print(texto_ajuda)
            resp=str(input('Qual sua resposta?!'))
    elif resp=='pula':
        if pula==3:
            print('Não deu! Você não tem mais direito a pulos!')
        elif pula==2:
            pula+=1
            print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
        elif pula==1:
            pula+=1
            print('Ok, pulando! Você ainda tem 1 pulo!')
        elif pula==0:
            pula+=1
            print('Ok, pulando! Você ainda tem 2 pulos!')
    elif resp=='parar':
        decidiu_parar=1
        #add umas coisas!!!
        break
    if resp==alternativa_correta:
        acertou_quantas_vezes+=1
        valor=lista_valores[acertou_quantas_vezes]
        print(f'Você acertou! Seu prêmio atual é de R$ {valor}.00')