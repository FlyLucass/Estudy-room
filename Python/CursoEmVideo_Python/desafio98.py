import time;

def contador():
    def stand():time.sleep(1)
    print("Contagem de 1 a 10: ")
    for i in range(1,11):
        print(i,end=' ',flush=True)
        stand()
    print('FIM!!') 
    
    
    print("\n\nContagem de 10 a 0: ")
    for i in range(10,0,-2):
        print(i,end=' ',flush=True)
        stand()
    print('FIM!!')    

    print("\n\nAgora uma contagem personalizada!!!")
    nubrs=[]
    nubrs.insert(1,int(input("Digite um número para inicia: ")))        
    nubrs.insert(2,int(input("Digite um número para final: ")))
    nubrs.insert(3,int(input("Digite um número para o intevarlo: ")))
    if nubrs[0]>nubrs[1]:
        nubrs[2]=-nubrs[2]
    if nubrs[2]==0:
        nubrs[2]=1
      
    print("\n\nA sua contagem personalizada é: ")
    for i in range(nubrs[0],nubrs[1],nubrs[2]):
        print(i,end=' ',flush=True)
        stand()
    print('FIM!!') 
        
        
    
    
contador()

