dados={}

nome=str(input("Digite seu nome: "))
dados={'Nome':nome}

media=float(input("Digite sua média: "))
dados['Média']=media

if media>=6:dados.update({'Situação':'Aprovado'})
else: dados.update({'Situação':'Reprovado'})

print(f"Olá {dados['Nome']}, sua média é: {dados['Média']}, portanto, sua situação é: {dados['Situação']}")