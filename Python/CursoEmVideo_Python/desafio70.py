nome=""
preco=float(0)
continuar=str("")
total_de_gasto=float(0)
produtos_plus_1000=int(0)
produto_mais_barato=str("")
produto_mais_barato_value=float(0)

while True:
    nome=input("Digite o nome do produto: ").capitalize()
    preco=float(input("Digite o valor dele: "))
    total_de_gasto+=preco
    if preco>=1000:produtos_plus_1000+=1
    if produto_mais_barato=="" and produto_mais_barato_value==0:
        produto_mais_barato_value=preco
        produto_mais_barato=nome
    else:
        if preco<produto_mais_barato_value:
            produto_mais_barato_value=preco
            produto_mais_barato=nome
    continuar=input("Você que continuar o programa? (S/N) ").lower()
    if continuar=="n": break

print(f"O total gasto é: R${total_de_gasto} \n{produtos_plus_1000} Custam acima de R$1000 \nO produto mais Barato e:  {produto_mais_barato}, custando {produto_mais_barato_value}")


  





