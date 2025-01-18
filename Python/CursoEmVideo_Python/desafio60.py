fat=int(input("Digite um numero inteiro: "))
fatorial=fat
i=int(fat-1)
while i!=1:
    fat=fat*i
    i=i-1

print(f"O fatorial de {fatorial}! é {fat}")