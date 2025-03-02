lista_all=[]
lista_girls=[]
continu=str('')
media=float(0)
contador_cad=int(0)

while not continu=='N':
    dictemp={}
    nome=str(input("Nome: ")).capitalize()
    dictemp.update({'Nome':nome})
    sexo=str(input("Sexo(M/F): ")).upper()
    if sexo=='F':
        lista_girls.append(nome)
    else:pass
    dictemp.update({'Sexo':sexo})
    idade=int(input("Idade: "))
    dictemp.update({'Idade':idade})
    media+=idade
    contador_cad+=1
    lista_all.append(dictemp.copy())
    dictemp.clear()
    continu=str(input("Que continuar(S/N): ")).upper()
    if continu!='N' and continu!='S':
        while continu!='N' and continu!='S':
            continu=str(input("Apenas(S/N): ")).upper()

media=media/contador_cad

print('-='*50)
print(f"Foram cadastrada {contador_cad} pessoa(s), a média de idade do grupo foi: {media}")
if lista_girls!=[]:
    print("As mulheres cadastradas foram: ",end='')
    for p in lista_girls:
        print(f"[{p}]",end="")
else:print("Não foram cadastradas mulheres!!!",end='')

lista_media_acima=[]
for i in lista_all:
   for val in i.values():
        if i['Idade']>media:
            lista_media_acima.append(i.copy())
            break


if lista_media_acima!=[]:
    print("\nAs pessoa(s) com idade acima da média são:")
    for p in lista_media_acima:
        print(f"{p['Nome']} com {p['Idade']} anos")
else:print("\nNão tem pessoas com idade acima da média")
        




