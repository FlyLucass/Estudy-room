print('Hello World!')
print(11+6)
print('5'+'5')

nome='lucas'
idade=18
peso=58
print(nome,idade,peso)
'''
nome=input('Qual o seu nome')
idade=input('qual a sua idade')
peso=input('quanto você pesa')
print(nome,idade,peso)

print('Bem vindo'','+nome)

print('Vamos começa, me fale sua data de nascimento no seguinte formato: Dia/data/ano')
Dia=input('Dia')
Mes=input('Mês')
Ano=input('ano')
print('OK!'' ''Sua data de nascimento e essa:',Dia,'/',Mes,'/',Ano)
input('Correto?')

print('Soma de Números')
numb1=int(input('Digite o 1° número'))
numb2=int(input('Digite o 2° número'))
soma=numb1+numb2
#forma  antiga: print('A soma entre',numb1,'+',numb2,'é:',soma) 
print('A soma entre {}+{} é: {}'.format(numb1,numb2,soma))# forma mais short com (.format) mais atual

'''

'''
print('Calculadora de números')
N1=int(input('Digite o 1°Número'))
N2=int(input('Digite o 2°Número'))
resul=N1+N2
print(f'A soma entre:{N1} é {N2}= {resul}')
'''

print('Check do que e digitado')
cite=input('Digite algo')
print('{} {}'.format('Qual o tipo?',type(cite)))
print('{} {}'.format('isso é feito em letra:',cite.isalpha()))
print('{} {}'.format('é em número:',cite.isnumeric()))


