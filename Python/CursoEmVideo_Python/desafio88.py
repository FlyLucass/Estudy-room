import random;
palpites=[]
palpites_stby=[]
quantidade_de_jogos=int(input("Quantos jogos você deseja? "))
contador=int(0)


while not quantidade_de_jogos==contador:
    for g in range(6):
        nub=random.randrange(1,61)
        if nub in palpites_stby: 
            while nub in palpites_stby:
                nub=random.randrange(1,61)
        else: palpites_stby.append(nub) 
        
    palpites.append(palpites_stby[:])
    palpites_stby.clear()
    contador+=1

print(f"Você solicitou {quantidade_de_jogos} palpites para Jogar: ")
print("\n")
for x in palpites:
    print(x)



