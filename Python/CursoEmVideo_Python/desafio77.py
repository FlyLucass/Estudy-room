palavras=('lucas', 'santos')


#esse "FOR" pecorre os indices da var >PALAVRAS
for i in palavras:
    print(f"\nNa palavra {i} temos as vogais: ", end='')
#esse FOR pecorre os Indice de cada PALAVRA
    for palavras in i:
        if palavras.upper() in 'AEIOU' :
            print(palavras.upper(),end=' ')


    



        
    
    
    
    
    
    
    
    
    
    
    
   
