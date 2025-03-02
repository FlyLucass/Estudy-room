import datetime;
dados={}

nome=str(input("Digite seu nome: "))
dados.update({'Nome:':nome})
ano_nasc=int(input("Digite seu ano de nascimento: "))
idade=datetime.now().year-ano_nasc
dados.update({'Idade:':idade})
ctps=int(input("Digite sua CTPS: "))
dados.update({'Ctps:':ctps})
if ctps!=0:
    ano_contrat=int(input("Qual foi o ano de contratação: "))
    dados.update({'Ano de contratação:':ano_contrat})
    salario=float(input("Qual o Salário? "))
    dados.update({'Salário:':salario})
    calc=35-(datetime.now().year-ano_contrat)
    aposet=idade+calc
    dados.update({'Aposetadoria em:':aposet})
else:pass

for i,v in dados.items():
    print(i,v)
