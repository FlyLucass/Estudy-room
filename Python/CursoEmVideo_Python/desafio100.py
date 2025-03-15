import random;
import time;

def sorteia(lista_nubrs):
    for i in range(1,6):
        lista_nubrs.append(random.randint(0,10))
    print("Os números sorteados foram:") 
    for v in lista_nubrs:
        print(v,end=' ',flush=True)
        time.sleep(0.5)
    print("OK!")
        
lista_nubrs=[]   
sorteia(lista_nubrs)
print('_-_'*19)

def somapar():
    soma_pares=int(0)
    for i in lista_nubrs:
        if i%2==0:
            soma_pares+=int(i)
    print(f"\nA soma dos números pares é: {soma_pares}")

somapar()

