i=int(2)
termos_var=int(0)
var_termos=int(1)
proximo=int(0)
i_user=int(input("Digite um numero inteiro: "))
print(termos_var)
print(var_termos)

while  i!=i_user:
   
    i+=1
    proximo=termos_var+var_termos
    print(proximo)
    termos_var=var_termos
    var_termos=proximo
    proximo=int(0)
    
    

   
