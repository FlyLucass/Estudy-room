numeros_digitados=[]
numeros_impares=[]
numeros_pares=[]

for i in range(1,8):
    numeros_digitados.append(int(input(f"Digite o {i}° valor: ")))

for v in numeros_digitados:
    print(v)
    if v%2==0: numeros_pares.append(v)
    else:numeros_impares.append(v)

numeros_impares.sort()
numeros_pares.sort()

print(f"Os números digitados foram{numeros_digitados} \nOs numeros PARES são:{numeros_pares} \nEntre,os IMPARES são: {numeros_impares}")

