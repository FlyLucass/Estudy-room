times=('','Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthians','Bahia','Cruzeiro','Vasco da Gama','Vitória','Atlético-MG','Fluminense','Grêmio','Juventude','Red Bull Bragantino','Athletico-PR','Criciúma','Atlético-GO','Cuiabá')


print("Os 5° Primeiros Colocados é: ")
for primeiros in range(1,6):
    print(primeiros, times[primeiros])

print("\nOs 4° Ultimos colocado da tabela: ")
for ultimos in range(17,len(times)):
    print(ultimos, times[ultimos])

#quando utilizado a função 'SORTED', a tupla e trasformada para listra
listra_ordenada=sorted(times)
print("\nListra ordenada: ")
for orden in range(1,len(listra_ordenada)):
    print(listra_ordenada[orden])


if  'Chapecohece' in times: print(f"\nA Chapeconhece se encontrar na posição: {times.index('Chapecohece')}°")
else: print("\nChapecohece não aparece entre os 20° primeiros colocados ")

