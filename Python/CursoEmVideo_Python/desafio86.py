matriz=[]
matriz_staby=[]
contador_direita=int(0)
contador_esquerda=int(0)

while len(matriz)!=3:
    while not contador_direita==3:
        nub=int(input(f"Digite um numero para posição [{contador_esquerda}][{contador_direita}] da matriz: "))
        matriz_staby.append(nub)
        contador_direita+=1
    matriz.append(matriz_staby[:])
    matriz_staby.clear()
    contador_direita=int(0)
    contador_esquerda+=1
print("Segue a matriz 3x3")
for v in matriz:
    for inde in v:
        print(f"[{inde}]",end='')
    print("\n")  

