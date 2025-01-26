idade= maior_18age= m = w_minus20  =int(0) 
sexo= sim_or_nao=  str("")

while True:
    idade=int(input("Digite sua Idade "))
    sexo=str(input("Digite seu Sexo "))
    sexo=sexo.lower()
    if sexo!="masculino" and sexo!="feminino":
        while True:
            sexo=str(input("Digite seu Sexo "))
            sexo=sexo.lower()  
            if sexo=="masculino"  or sexo=="feminino":break
             
    if idade>18: maior_18age+=1
    if sexo=="masculino": m+=1
    if sexo=="feminino" and idade<20:w_minus20+=1

    sim_or_nao=str(input("Você deseja continua cadastrando mais pessoas? (responda com S/N ) "))
    sim_or_nao=sim_or_nao.upper()
    if sim_or_nao!="S" and sim_or_nao!="N":
        while True:
           sim_or_nao=str(input("Você deseja continua cadastrando mais pessoas? (responda com S/N ) "))
           sim_or_nao=sim_or_nao.upper() 
           if sim_or_nao=="S" or sim_or_nao=="N":break

    if sim_or_nao=="N" : break

print(f"Foran cadastrado(s) {maior_18age} com a idade acima de 18 anos \nExistem {m} Homen(s) cadastrado(s) \nExistem {w_minus20} mulhere(s) cadastradas, abaixo de 20 anos")