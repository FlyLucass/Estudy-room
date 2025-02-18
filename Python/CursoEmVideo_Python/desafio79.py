nubrs=[]
continua=str('')

while continua!='N':
    nub=int(input("Digite um número: "))
    if nub in nubrs:
        while nub in nubrs: 
                nub=int(input("Esse numero ja exite na lista \nDigite um número novo: "))
    else:pass
    nubrs.append(nub)
    continua=str(input("Que continuar(S/N): ")).upper()
    if continua!='N' and continua!='S':
         while continua!='N' and continua!='S':
            continua=str(input("Não existe essa opção \nDigite(S/N): ")).upper()
    else:pass

nubrs.sort()

print("Os numeros digitados foram: ", end=" ")
for i in range(0,len(nubrs)):
    print(nubrs[i],end=' ')
    
    


