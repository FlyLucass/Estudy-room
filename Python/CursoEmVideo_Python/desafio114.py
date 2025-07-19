import requests;

def design():
    print(f"{'='*40}")


try:
   site=requests.get('https://www.pudim.com.br/')
except:
    design()
    print("  Houve um problema ao acessar o site") 
    design()
else:
    design()
    print("\tSite acessado com sucesso") 
    design()
 