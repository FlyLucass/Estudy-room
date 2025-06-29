def fatorial(numero=1,show='False'):
    
    '''
    ESCOLHAR O NÚMERO, PARA DESCOBRIR O FATORIAL
    APÓS FICA A DECISÃO PARA MOSTRAR NA TELA:
    TRUE:SIM
    FALSE:NÃO
    '''
    
    
    if show=='True':
        show=[]
        for i in range(numero,0,-1):
            if i!=1: print(f"{i}X",end='')
            else: print(f"{i}: ",end='')
        if numero!=1:
            for i in range(numero,1,-1):
                numero=numero*(i-1)
            print(numero)
        else: print(numero)

    else:
        print(f"O fatorial de {numero}! é: ",end='')
        if numero!=1:
            for i in range(numero,1,-1):
                numero=numero*(i-1)
            print(numero)
        else: print(numero)
           
        
    
    
nub=int(input("Digite um número: "))
most=str(input("Você que mostrar na tela o processo(TRUE/FALSE): ")).capitalize()
fatorial(nub,most)

help(fatorial)
