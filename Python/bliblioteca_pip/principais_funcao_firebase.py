import requests;
'''
one='{"Name":"Lucas","Age":"19","Course":"ADS"}'
pt=requests.post("https://cot-day-default-rtdb.firebaseio.com/.json",data=one)

print(pt)
print(pt.json())

'''

#pegando os dados feito acima no FIREBASE
importando=requests.get("https://cot-day-default-rtdb.firebaseio.com/-OLR-wrhnxKhbvmLrHZN/.json")
print(f"{importando},{importando.json()}")

'''
#criando mas um json no banco de dados, semelhante para as modificações
test='{"Name":"Lucas","Age":"19","Course":"ADS"}'
pt=requests.post("https://cot-day-default-rtdb.firebaseio.com/.json",data=test)

print(pt)
print(pt.json())

'''
'''
#agora modificando as informações
mod='{"Name":"Desconhecido","Age": 19 ,"Course":"T.I"}'
pt=requests.patch("https://cot-day-default-rtdb.firebaseio.com/-OLR78DfVyZJ-UCTd8YZ/.json",data=mod)
print(pt,pt.json())

'''
#agora pegando essa modificação
importando=requests.get("https://cot-day-default-rtdb.firebaseio.com/-OLR78DfVyZJ-UCTd8YZ/.json")
print(f"{importando},{importando.json()}")


