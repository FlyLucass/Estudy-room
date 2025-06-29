import datetime;

def voto(ano):
    
    idade=(datetime.datetime.now().year)-ano
    if idade<16:idade="VOTO NEGADO!!!"
    elif idade>=18 and idade<65:idade="VOTO OBRIGATORIO!!!"
    else: idade="VOTO OPCIONAL!!!"
    return idade
    
idade=int(input("Digite o ano de nascimento: "))
print(f"{'-'*30} \n{voto(idade)}")