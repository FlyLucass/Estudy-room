aproveitamento_geral={}
contagem_jogadores=int(1)

while True:
    aproveitamento={}
   
    nome=str(input('Nome do jogador: ')).capitalize()
    aproveitamento['Jogador']=nome
    partidas=int(input("A quantidade de Jogos é: "))
    aproveitamento['Partidas']=partidas

    contador=int(1)
    gols=[]
    tot_gol=int(0)

    if partidas>0:
        while not partidas==0:
            gol=int(input(f"Quantos Gol(s) no {contador}° Jogo: "))
            gols.append(gol)
            tot_gol+=gol
            partidas-=1
            gol=int(0)
            contador+=1
    aproveitamento.update({'Total de Gol':tot_gol})
    aproveitamento.update({'Gol por partida':gols[:]})
    
    fim_ou_nao=str(input("Deseja continua o programa(S/N)? ")).upper()
    
    gol=int(0)
    gols.clear()
    tot_gol=int(0)
    partidas=int(0)
    nome=str('')
    contador=int(1)
    aproveitamento_geral.update({f'{contagem_jogadores}':aproveitamento.copy()})
    aproveitamento.clear()
    if fim_ou_nao!='N' and fim_ou_nao!='S':
        while fim_ou_nao!='N' and fim_ou_nao!='S':
            fim_ou_nao=str(input("Apenas:(S/N) ")).upper()
    if fim_ou_nao=='N':break
    contagem_jogadores+=1


print(f"Foram cadastrado {contagem_jogadores}")

contador=int(1)
for i in aproveitamento_geral.values():
        print(f"Código:{contador}",end=' / ')
        print(f"Jogador: {i['Jogador']}\tJogou: {i['Partidas']} partidas\tExecutado: {i['Total de Gol']} Gol(s)")
        contador+=1

while True:
    levantamento=str(input("Você que o levantamento de qual Jogador? "))
    if levantamento=='999':break
    if levantamento in aproveitamento_geral:
        print(f"Levantamento do jogador {aproveitamento_geral[levantamento]['Jogador']}: ")
        cont=int(1)
        for ler in aproveitamento_geral[levantamento]['Gol por partida']:
            print(f"No {cont}° jogo foram {ler} gol(s)")
            cont+=1
    
        




    
