import math;
import random;
import datetime;
import time;
import statistics;
import operator;

def linh_text(texto):
        print(texto)
        print('-='*30)
        


# dia=datetime.datetime.today().strftime('%d/%m')
# if dia=='28/12': print("feliz natal")
# else: print("ainda não e natal")

# #Validado de CPF, pelo tamanho
# cpf=()
# cpf=tuple(input("Digite um cpf "))
# t_cpf=len(cpf)
# if t_cpf == 11:print("Os numeros digitados formam um cpf")
# else:print("Esse numeros não formam um cpf")

# numeros=[0,1,2]

# for indice,nub in enumerate(numeros):
#     print(f"na posição {indice} o valor e {nub}")
# print("Apenas esses")

# pessoas= [ {'nome':'lucas'},
#         {'nome':'santos'}
#         ]
# linh_text(pessoas[0])
# linh_text(pessoas[1])

  
# def dobra(lst):
#         i=0
#         while i < len(lst):
#                 lst[i]*=2 
#                 i+=1     
         

# valores=[5,8,9]
# dobra(valores)
# print(valores)

# print(list.__doc__) #para verificar toda a cadeia da função
# # help(print)#para verificar toda a cadeia da função

# def contador(i=0,f=10,p=1): #parametros opcionais
#         """
#         i=inicio
#         f=fim
#         passo=de quanto em quanto
#         """
#         f=12 #escopo local
#         c=i
#         while c<=f:
#                 print(f'{c}',end='..')
#                 c+=p
#         print("Fim!")


# contador(i=0,f=10,p=3) #escopo global

# help(contador)

def num(b=0):
        global a
        a=9
        print(a)

a=int(5)
print(a) #saida 5, pois antes da função
num(a) #saida 9, depois da função, pois declara o a como 9


# def multipli(v1=0,v2=0):
#         global v2
#         v2=10
#         m=v1*v2
#         return m


# r1=multipli(1,6)
# r2=multipli(3,3)
# print(r1,r2)

#dar para chamar a função dentro do print





    

 













    







 







