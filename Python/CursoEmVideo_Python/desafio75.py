nub=[]
nub_user_change=int(0)
nub_pares=[]

for i in range(1,5):
    nub_user_change=int(input(f"digite o {i}° numero "))
    nub.append(nub_user_change)

nub=tuple(nub)
print(f"\nOs numero digitados foram {nub}")
print(f"O número nove apareceu {nub.count(9)} vezes")
if 3 in nub:print(f"O primeiro 3,apareceu na posição {nub.index(3)}")
else:print("não houve a digitação do número 3")

for d in range(0,len(nub)):
    if nub[d]%2==0: nub_pares.append(nub[d])
    else:pass

nub_pares=tuple(nub_pares)
if nub_pares==():print("não houve a digitação de numeros pares ")
else:print(f"Os número PARES disgitados foram: {nub_pares}")




