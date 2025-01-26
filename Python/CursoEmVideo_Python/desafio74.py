import random;
nbrs=()
nub_ger=int()


for n in range(1,6):
    nub_ger=random.randrange(0,11)
    nub_ger=(nub_ger,)
    nbrs=nbrs+nub_ger

print("NUMEROS GERADOS LISTRADOS: ")
for i in range(0,len(nbrs)):
    print(nbrs[i], end=',')

print("\nMaior número encontrado entre os 5 é: {}".format(max(nbrs)))
print("Menor número encontrado entre os 5 é: {}".format(min(nbrs)))