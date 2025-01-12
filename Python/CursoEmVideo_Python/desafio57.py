genero=""
while genero !="M" and genero !="N" and genero!="F":
    genero=input("Digite seu genero, com M, F, N(Nenhuma das opções anteriores): ").upper()
if genero=='M':print("Seu genero e Masculino")
elif genero=='F':print("Seu genero e Feminino")
else:print("Você não se indetificar com nenhum dos generos")