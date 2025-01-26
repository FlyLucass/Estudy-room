import random;

print("vamos jogar Jokenpô")
escolcompt=random.choice(["pedra","papel","tesoura"])
escoluser=input("Escolhar entre pedra, papel e tesoura: ")
escoluser=escoluser.casefold()
if escoluser==escolcompt:print("Não houve ganhadores")
elif escolcompt=="pedra" and escoluser=="papel":print("Você ganhou do computador")
elif escolcompt=="papel" and escoluser=="tesoura":print("Você ganhou do computador")
elif escolcompt=="tesoura" and escoluser=="pedra":print("Você ganhou do computador")
else:print("O computador ganhou de você")