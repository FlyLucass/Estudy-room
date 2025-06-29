def aumentar(valor,plus,f=True):
    plus_new_valor= valor+((plus/100)*valor)
    if f==True: 
        return moeda(plus_new_valor)
    else:
        plus_new_valor=valor+((plus/100)*valor)
        return plus_new_valor


def diminuir(valor,minus,f=True):
    if f==True:
        minus_new_valor=valor-((minus/100)*valor)
        return moeda(minus_new_valor)
    else:
        minus_new_valor=valor-((minus/100)*valor)
        return minus_new_valor

def dobro(valor,f=True):
    if f==True: 
        dobro=valor*2
        return moeda(dobro)
    else:
        dobro=valor*2
        return dobro
    

def metade(valor,f=True):
    if f==True:
        metade=valor/2
        return moeda(metade)
    else:
        metade=valor/2
        return metade

def moeda(v):
    formatado=f"R$: {v:.2f} "
    formatado=formatado.replace('.',',')
    return formatado

def prog():

    prog_funções= '''
    Função aumentar(valor,plus):
    Recebe dois parametros: VALOR= valor monétario do usúario / PLUS= valor em porcetagem que você deseja aumetar
    
    Função diminuir(valor):
    Recebe dois parametros: VALOR= valor monétario do usúario / MINUS= valor em porcetagem que você deseja diminuir
    
    Função dobro(valor):
    Recebe um parametro: VALOR= valor monetario do usuario
    
    Função metade(valor):
    Recebe um parametro: VALOR= valor monetario do usuario
    
    '''

    return prog_funções

def resumo(valor,porcen,f=False):
    if f==True:print(f"O valor {moeda(valor)} ")
    else:print(f"O valor {valor} ")
    print(f"Aumentou {aumentar(valor,porcen,f)} ")
    print(f"Diminuiu {diminuir(valor,porcen,f)} ")
    print(f"Dobro {dobro(valor,f)} ")
    print(f"Metade {metade(valor,f)} ")




