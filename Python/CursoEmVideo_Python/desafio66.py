nub=int(0)
soma=int(0)
i_nubrs=int(0)

while True:
    nub=int(input("Digite uns números: (lembrado que o número 999, pausa o códico)"))
    if nub==999:break  
    i_nubrs+=1 
    soma+=nub
print(f"Foram digitados {i_nubrs} números, a soma deles e {soma}")
    