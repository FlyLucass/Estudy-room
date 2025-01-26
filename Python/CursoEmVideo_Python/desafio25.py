import random;

nubcomputer= random.randint(0,5)
print(nubcomputer)
nubuser=int(input("Vamos ver se voce adivinha o numero que a maquina está armazenando \nQual o numero voce achar que ele armazenou entre 0 e 5? "))
if nubcomputer==nubuser:print("Voce venceu, o computador pensou no nuumero: {}".format(nubuser))
else: print("Voce perdeu!!")