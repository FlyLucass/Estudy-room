from UtilidadesCeV import moeda
from UtilidadesCeV import moeda_value

print(moeda.prog())

# valor_user=float(input("Digite um valor "))
# valor_em_porcetagem=float(input("Digite um valor em porcetagem "))

# print("O valor {} \nAumentou {} ".format(moeda.moeda(valor_user),moeda.aumentar(valor_user,valor_em_porcetagem,True)))
# print(f"Diminuiu {moeda.diminuir(valor_user,valor_em_porcetagem,False)}")
# print(f"Dobro {moeda.dobro(valor_user,True)} \nMetade {moeda.metade(valor_user,False)}" )

# moeda.resumo(valor_user,valor_em_porcetagem,True)


#entrada apenas com input
valor_user=input("Digite um valor ")
valor_em_porcetagem=input("Digite um valor em porcetagem ")
moeda_value.leiadinheiro(valor_user,valor_em_porcetagem,True)

