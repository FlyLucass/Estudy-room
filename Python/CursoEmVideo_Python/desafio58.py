import random;


nubcomputer= random.randint(0,10)
print(nubcomputer)
n_vezes=int(0)
nubuser=int(input("Vamos ver se voce adivinha o numero que a maquina está armazenando \nQual o numero voce achar que ele armazenou entre 0 e 10? "))
while not nubuser==nubcomputer:
    n_vezes+=1
    nubuser=int(input("Você errou!! \ntente novamente: "))
if n_vezes != 0: print(f"Você precisou de {n_vezes} tentativa(s)")
else:print("Você acertou de primeira")










