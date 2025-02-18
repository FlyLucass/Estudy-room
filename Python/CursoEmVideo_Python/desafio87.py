matriz=[]
matriz_staby=[]
contador_direita=int(0)
contador_esquerda=int(0)
some_all_nubrs_pares=int(0)
soma_all_terceira_coluna=int(0)



while len(matriz)!=3:
    while not contador_direita==3:
        nub=int(input(f"Digite um numero para posição [{contador_esquerda}][{contador_direita}] da matriz: "))
        if nub%2==0:some_all_nubrs_pares+=nub
        matriz_staby.append(nub)
        contador_direita+=1
        if contador_direita==3: soma_all_terceira_coluna+=nub
    matriz.append(matriz_staby[:])
    matriz_staby.clear()
    contador_direita=int(0)
    contador_esquerda+=1
    
print("Segue a matriz 3x3")
for v in matriz:
    for inde in v:
        print(f"[{inde}]",end='')
    print("\n")  

print(f"A soma de todos os números pares é: {some_all_nubrs_pares}")
print(f"A soma dos valores da 3° Coluna é: {soma_all_terceira_coluna}")
print(f"O maior número da 2° Linha é: {max(matriz[1])}")
