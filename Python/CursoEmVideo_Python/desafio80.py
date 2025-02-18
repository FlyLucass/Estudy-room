import bisect;
#FEITO COM AJUDA, DE UMA MANEIRA AUTOMATIZADA COM UM MODULO
numeros_user=[]

for i in range(1,6):
    num=int(input(f"Digite o {i}° numero: "))
    bisect.insort(numeros_user,num)

print(numeros_user)


    
