nubs=[]
end_alg=str('')
cont=int(1)

while not end_alg=='NÃO':
    nubs.append(int(input(f"Entre com o {cont}° valor: ")))
    end_alg=str(input("Que continuar o prog(SIM OU NÃO)?: ")).upper()
    if end_alg!='NÃO' and end_alg!='SIM':
        while end_alg!='NÃO' and end_alg!='SIM':
            end_alg=str(input("Apenas SIM ou NÃO, por favor: ")).upper()
    else:pass
    cont+=1

nubs.sort(reverse=True)
print(f"\nO total de número digitados é: {len(nubs)}\nA lista em ordem decrecente é: {nubs}")
if 5 in nubs:  
    print(f"O valor 5, foi digitado {nubs.count(5)}")
else: print("não foi digitado o número 5")