def leiaint(nub):
    try:
        nub=int(nub)
  
    except ValueError:
        nub=input("Valor invalido, digite um número inteiro: ")
        leiaint(nub)
     
    else:
        print(f'{'-'*30}')
        print(f"O número inteiro digitado foi {nub}")

def leiafloat(num):
    try:
        num=float(num)   
    except ValueError:
        num=input("Valor invalido, digite um número do tipo float: ")
        leiafloat(num)
    else:
        print(f"O valor digitado do tipo float foi {num}")
    
        
nub_user_int=input("Digite um número inteiro: ")
nub_user=input("Digite um número float: ")

leiaint(nub_user_int)
leiafloat(nub_user)

