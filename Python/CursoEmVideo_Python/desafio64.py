nubrs=int(0)
nub_user=int(0)
soma=int(0)

while nub_user!=999:
    nub_user=int(input("Digite um numero: (lembrando que a condição de parada e 999) "))
    nubrs+=1
    if nub_user!=999:
        soma+=nub_user
    else:pass
    
  
    
print("Foram digitados {} numeros\nA soma entre eles foram {}".format(nubrs,soma))

