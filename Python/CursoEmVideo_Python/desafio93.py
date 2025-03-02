aproveitamento={}
nome=str(input("Nome do Jogador: "))
aproveitamento.update({'Jogador':nome})
parti=int(input("Quantas partidas ele jogou: "))
aproveitamento.update({'Partidas':parti})

gols=[]
contador_parti=int(0)
contador=int(1)
tot_gol=int(0)
if parti!=0:
    while not parti==contador_parti:
        gol=int(input(f"Quantos gols foram no {contador}° jogo: "))
        gols.append(gol)
        tot_gol+=gol
        contador+=1
        contador_parti+=1

aproveitamento.update({'Total de Gol':tot_gol})
aproveitamento.update({'Gol por partida':gols})


contador=int(1)

print(f"O jogador {aproveitamento['Jogador']}, jogou {aproveitamento['Partidas']} partidas")
if aproveitamento['Partidas']>0:
    print("Realizando {} Gol(s) no total".format(aproveitamento['Total de Gol']))
    if aproveitamento['Total de Gol']!=0:
        for i in aproveitamento['Gol por partida']:
            print(f"No {contador}° jogo foram: {i} gol(s)")
            contador+=1

