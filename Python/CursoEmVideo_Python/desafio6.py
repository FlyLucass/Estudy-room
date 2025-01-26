import math;
print("Vamos calcular a hipotenusa!\n")
catopos=float(input("Qual o valor do cateto oposto? "))
catadjacete=float(input("E o do cateto adjacete? "))
print("A hipotenusa e: {}".format(math.hypot(catadjacete,catopos)))