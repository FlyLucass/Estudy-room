nub_user=int(0)
nubs_max_min=[]
soma_media=int(0)
r_user=""
i_nub=int(0)

while not r_user=="N":
    nub_user=int(input("Digite um numero: "))
    nubs_max_min.append(nub_user)
    soma_media+=nub_user
    i_nub+=1
    r_user=input("Deseja continuar o programa?[S/N] ")
    r_user=r_user.upper()

soma_media=soma_media/i_nub

print("A media dos numero e: {} \nO maior numero Digitado foi:{} \nO menor foi: {}".format(soma_media,max(nubs_max_min),min(nubs_max_min)))





    


    
    
   


