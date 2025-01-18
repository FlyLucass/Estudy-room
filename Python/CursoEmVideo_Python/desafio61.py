termo_1=int(input("Digite o primeiro termo da PA: "))
pa=int(input("Digite a razão: "))
i=int(1)

print(f"\nO primeiro termo e: {termo_1}")
while i!=10:
    termo_1=termo_1+pa
    print(termo_1)
    i+=1
