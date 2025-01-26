import random;

nub_had=int(0)
nub_user=int(0)
esco_had=str("")
esco_user=str("")
ganhador=str("")
vit_user=int()

while True:
#MODULO RANDOM GERA UM NUMERO ALEATORIO PARA A VAR 
    nub_had=int(random.randint(0,11))
    print(nub_had)
##RECEBE O VALOR DO USUARIO E COMPARA SE E MAIOR QUE 10, CASO SIM, ENTRAR EM LOOPING ATE QUE SEJA ABAIXO DE DE 10
    nub_user=int(input("Digite um valor entre 0 e 10 "))
    if nub_user>10:
        while True:
            nub_user=int(input("Digite um valor entre 0 e 10 "))
            if nub_user<11:break

##RECEBE OUTRO VALOR DO USUARIO, CASO SEJA UM VALOR FORA DO COMUM, ENTRAR EM LOOPING, ATE QUE SEJA AS OPCOES REPASSADA
    esco_user=str(input("Digite qual você escolhe entre PAR E IMPAR: "))
    esco_user=esco_user.upper()
    if esco_user!= "PAR" and esco_user!="IMPAR":
        while True:
            esco_user=str(input("Digite qual você escolhe entre PAR E IMPAR: "))
            esco_user=esco_user.upper()
            if esco_user== "PAR" or esco_user=="IMPAR":break

##POR FIM COMPARAR OS VALORES, E VER O GANHADOR
    if esco_user=="PAR": esco_had=str("IMPAR")
    else: esco_had=str("PAR")
    if (nub_had+nub_user) %2==0:ganhador=str("PAR")
    else: ganhador=str("IMPAR")
    if ganhador==esco_user:
        vit_user+=1  
    else:break

if vit_user>0: print(f"Você Perdeu!!! \nPorém Ganhou {vit_user} Vezes")
else:print("Você perdeu!!!")



