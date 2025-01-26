nubs=[]
for inde in range(1,6):
    nubs.append(float(input(f"DIgite o {inde}° Numero: "))) #não coloca "==" para atribuir pois tem a função append fazendo o mesmo! 
print(f"O maior peso é: {max(nubs)} \nE o menor peso é: {min(nubs)}")