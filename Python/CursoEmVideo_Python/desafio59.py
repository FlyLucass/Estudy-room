import math;

value1=float(input("Digite o 1° valor "))
value2=float(input("Digite o 2° valor "))
escolh=int(0)

while escolh !=5:
    escolh=int(input("1º Somar \n2º Multiplicar \n3º Maior \n4º Novos numeros \n5º Sair do programa \nESCOLHAR: "))
    if escolh==1 : 
        somar=value1+value2
        print(f"\n A soma dar {somar}\n")
    
    elif escolh==2:
        multiplicar=value2*value1
        print(f"\na multipicação dos dois numeros e: {multiplicar}\n")

    elif escolh==3:
        maior=max(value2,value1)
        print(f"\nO maior e {maior}\n")  

    elif escolh==4:
        value1=float(input("Digite o 1° valor "))
        value2=float(input("Digite o 2° valor "))
    



print("Programa encerrado")

    

