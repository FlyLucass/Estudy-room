
def ficha(nome,gols):
    if gol==0:
        print(f"O jogador {nome}, não fez nenhum gol")
    elif gol==1:
        print(f"O jogador {nome}, fez {gols} gol")
    else:
        print(f"O jogador {nome} marcou {gols} gols ")



name=str(input("Digite seu nome: ")).capitalize()
gol=input("Quantos gols foram marcado por você? ")
if name=='':
    name='Desconhecido'
if gol=='':
    gol=0
gol=(int(gol))
ficha(name,gol)