nubrs=[]
continua=str()

while not continua=='n':
    nubrs.append(int(input("Entre com o valor: ")))
    continua=str(input("Que continuar o Algoritmo(S/N): ")).lower()
    if continua!='n' and continua!='s':
        while continua!='n' and continua!='s':
            continua=str(input("Essa opção não existe, apenas(s/n): ")).lower()

nubrs_par=[]
nubrs_impares=[]

for i,n in enumerate(nubrs):
    if n%2==0: nubrs_par.append(n)
    else: nubrs_impares.append(n)

nubrs_par.sort()
nubrs_impares.sort()

print(f"Números Digitados:{nubrs} \nNúmeros pares:{nubrs_par} \nNúmeros impares{nubrs_impares}")





