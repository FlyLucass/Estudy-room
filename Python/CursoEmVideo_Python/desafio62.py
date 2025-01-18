termo_1=int(input("Digite o primeiro termo da PA: "))
pa=int(input("Digite a razão: "))
i=int(1)

print(f"\nO primeiro termo e: {termo_1}")
while i!=10:
    termo_1=termo_1+pa
    print(termo_1)
    i+=1
    if i==10:
        i=int(input("Você deseja mais quntos termos: "))
        if i ==0: break
        else:pass
print("Programa encerrado!!!")

 