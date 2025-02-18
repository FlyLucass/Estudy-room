value_nub=[]

for i in range(1,6):
    value_nub.append(int(input(f"Digite o {i}° número: ")))

minimo=int(min(value_nub))
maximo=int(max(value_nub))
i_maximo=[]
i_minimo=[]

for p,nub in enumerate(value_nub):
        if maximo == nub:i_maximo.append(p)
        if minimo == nub:i_minimo.append(p)
        else:pass
        


print(f"Os numeros digitados foram: {value_nub}")
print(f"o maior numero digitado foi {maximo} encontrado em: {i_maximo}")
print(f"o menor numero digitado foi {minimo} encontrado em: {i_minimo}")

    

