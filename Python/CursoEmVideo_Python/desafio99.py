import time;
def nubrs(*maior_nub):
    print("-"*30)
    print(f"Foram digitados {len(maior_nub)} números")
    print("Os números digitados foram: ", end='')
    for i,v in enumerate(maior_nub):
        print(v,end=' ',flush=True)
        time.sleep(0.2)
        
    print(f"... \nO maior número é {max(maior_nub)}")

nubrs(9,8,6,5,3,2,1)
nubrs(50,40)
    
    
