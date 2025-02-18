nome_peso=[]
continue_as=str('')
dados=[]

while continue_as!='N':
    nome=str(input("Digite seu nome: "))
    nome_peso.append(nome)
    peso=float(input("Digite seu peso: "))
    nome_peso.append(peso)
    dados.append(nome_peso[:])
    nome_peso.clear()
    continue_as=str(input('Que continua? (S/N)')).upper()
    if continue_as!='S' and continue_as!='N':
        while continue_as!='S' and continue_as!='N':
            continue_as=str(input("Apenas (S/N), que continua o programa? ")).upper()



print(f"\nForam cadastradas {len(dados)} Pessoas")

pessoa_mais_pesada=[]
pessoa_menos_pesada=[]

for i in range(0,len(dados)):
    if i==0:
        pessoa_mais_pesada.append(dados[0][1])
        pessoa_mais_pesada.append(dados[0][0])
    else:
        if dados[i][1]>pessoa_mais_pesada[0]:
           pessoa_mais_pesada[0]=dados[i][1]
           pessoa_mais_pesada[1]=dados[i][0]
        elif dados[i][1]==pessoa_mais_pesada[0]:
            pessoa_mais_pesada.append(dados[i][0]) 
        else:pass

print(f"O maior peso registrado foi: {pessoa_mais_pesada[0]} KG, sendo a(s) seguite(s) pessoa(s): ",end='')
for i in pessoa_mais_pesada[1:]:
    print(f"[{i}]", end=' ')



for inde in range(0,len(dados)):
    if inde==0:
        pessoa_menos_pesada.append(dados[0][1])
        pessoa_menos_pesada.append(dados[0][0])
    else:
        if dados[inde][1]<pessoa_menos_pesada[0]:
            pessoa_menos_pesada[0]=dados[inde][1]
            pessoa_menos_pesada[1]=dados[inde][0]
        elif dados[inde][1]==pessoa_menos_pesada[0]:
            pessoa_menos_pesada.append(dados[inde][0])
        else:pass

print(f"\nO menor peso entre os dados é: {pessoa_menos_pesada[0]} KG, com o(s) seguite(s) nome(s): ",end='')
for v in pessoa_menos_pesada[1:]:
    print(f"[{v}]",end=' ')






           
        



        
    

 

    









