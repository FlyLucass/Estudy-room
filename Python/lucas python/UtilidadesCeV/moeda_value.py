from . import moeda

def moeda_formatada(v):
    formatado=f"R$: {v:.2f} "
    formatado=formatado.replace('.',',')
    return formatado

def leiadinheiro(valor,porce,deci=False):
    if valor.isnumeric()==True and porce.isnumeric()==True:
        valor=float(valor)
        porce=float(porce)
        moeda.resumo(valor,porce,deci)
    else:
        print("Não foi digitado um valor monetário, em algum dos campos\n")
        while valor.isnumeric()!=True or porce.isnumeric()!=True:
            valor=input("Entre com um valor: ")
            porce=input("Uma porcetagem a ser atribuida ao valores:")
        valor=float(valor)
        porce=float(porce)
        moeda.resumo(valor,porce,deci)

    
        
        
        
        
    




   
    
        
        