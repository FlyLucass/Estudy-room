termo_1=int(input("Digite o 1° termo da P.A: "))
razao=int(input("Qual a razão? "))
print(f"o primeiro termo é: {termo_1}")
for i in range(1,11): 
    termo_1=termo_1+razao
    print(termo_1)