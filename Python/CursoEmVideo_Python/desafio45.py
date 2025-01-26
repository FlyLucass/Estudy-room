plus=int(0)
minus=int(0)
for indi in range(1,8): 
    anonasc=int(input(f"Digite o {indi}° ano de nascimmento: "))
    anonasc=2024-anonasc
    if anonasc>=18: plus+=1;anonasc==0
    elif anonasc<18: minus+=1;anonasc==0
print("{} atingiram a maioridade e {} não atingiram, ainda".format(plus,minus))
