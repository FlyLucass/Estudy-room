produtos_e_precos=('Cafe',15,'Arroz',6,'Biscoito',3,'Feijão',8)

for i in range(0,len(produtos_e_precos),2):
    print(f"{produtos_e_precos[i]} \tR$: {produtos_e_precos[i+1]:.2f}")
    
