import random;
import time;
import operator;
value_jog={}

for i in range(1,5):
    num=int(random.randrange(1,6))
    value_jog.update({f'{i}° Jogador':num})
    num=int(0)

for p,v in value_jog.items():
    print(f"O {p}, rolou {v}")
    time.sleep(1)
    
print(f"\n{"-"*30}\n")

rank=sorted(value_jog.items(), key=operator.itemgetter(1), reverse=True)

for p,v in enumerate(rank):
    print(f"Em {p+1}° lugar ficou o {v[0]} tirando {v[1]}")

#Algoritmo feito com ajuda do professor





