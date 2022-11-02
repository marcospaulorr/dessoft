def transforma_base(lista):
    final={}
    lista_nivel=[]
    for dic in lista:
        lista_nivel=[]
        if dic['nivel'] not in final:
            lista_nivel.append(dic)
            final[dic['nivel']]=lista_nivel[:]
        else:
            lista_nivel=final[dic['nivel']]
            lista_nivel.append(dic)
            final[dic['nivel']]=lista_nivel[:]
    return final


def valida_questao(dic):
    final={}
    lista_numeros=['1','2','3','4','5','6','7','8','9','0']
    alfabetomin=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
    lista_final=[]
    for letra in alfabetomin:
        letra=letra.upper()
        lista_final.append(letra)
    for n in lista_numeros:
        lista_final.append(n)
    for k in alfabetomin:
        lista_final.append(k)
    if len(dic)!=4:
        if 'titulo' not in dic:
            final['titulo']='nao_encontrado'
        if 'nivel' not in dic:
           final['nivel']='nao_encontrado'
        if 'opcoes' not in dic:
            final['opcoes']='nao_encontrado'
        if 'correta' not in dic:
            final['correta']='nao_encontrado'
        final['outro']='numero_chaves_invalido'
    if 'correta' in dic:
        if dic['correta'] not in ['A','B','C','D']:
            final['correta']='valor_errado'
    if 'titulo' in dic:
        if dic['titulo'].strip()=='':
            final['titulo']='vazio'
    if 'nivel' in dic:
        if dic['nivel']!='facil' and dic['nivel']!='medio' and dic['nivel']!='dificil':
            final['nivel']='valor_errado'
    if 'opcoes' in dic:
        opcoes={}
        items=dic['opcoes']
        if len(items)!=4:
            final['opcoes']='tamanho_invalido'
        else:
            a=0
            b=0
            c=0
            d=0
            for numero in lista_final:
                if a==0:
                    if numero in items['A']:
                        a=1
                if b==0:
                    if numero in items['B']:
                        b=1
                if c==0:
                    if numero in items['C']:
                        c=1
                if d==0:
                    if numero in items['D']:
                        d=1
            if a==0:
                opcoes['A']='vazia'
            if b==0:
                opcoes['B']='vazia'
            if c==0:
                opcoes['C']='vazia'
            if d==0:
                opcoes['D']='vazia'
        if len(opcoes)!=0:
            final['opcoes']=opcoes
    return final



import random
def gera_ajuda(dic):
    lista_incorretas=[]
    dic_opcoes=dic['opcoes']
    correta=dic['correta']
    for opcoes in dic_opcoes.keys():
        if opcoes!=correta:
            lista_incorretas.append(opcoes)
    n=random.randint(1,2)
    if n==1:
        item1=random.choice(lista_incorretas)
        gab1=dic_opcoes[item1]
        st=f'''DICA:\nOpções certamente erradas: {gab1}'''
    elif n==2:
        item1=random.choice(lista_incorretas)
        lista_incorretas.remove(item1)
        item2=random.choice(lista_incorretas)
        gab1=dic_opcoes[item1]
        gab2=dic_opcoes[item2]
        st=f'''DICA:\nOpções certamente erradas: {gab1} | {gab2}'''
    return st

def valida_questoes(lista):
    final=[]
    for questao in lista:
        valida=valida_questao(questao)
        final.append(valida)
    return final

import random
def sorteia_questao(dic,nivel):
    dicionario=dic[nivel]
    x=random.choice(dicionario)
    return x
def sorteia_questao_inedida(dic,nivel,lista):
    x=sorteia_questao(dic,nivel)
    while x in lista:
        x=sorteia_questao(dic,nivel)
    lista.append(x)
    return x

def questao_para_texto(dicionario,n):
    st=f'''----------------------------------------
QUESTAO {n}

{dicionario['titulo']}

RESPOSTAS:
A: {dicionario['opcoes']['A']}
B: {dicionario['opcoes']['B']}
C: {dicionario['opcoes']['C']}
D: {dicionario['opcoes']['D']}'''
    return st