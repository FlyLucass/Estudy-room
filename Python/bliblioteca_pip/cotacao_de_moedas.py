import requests;

btc_dolar=requests.get("https://economia.awesomeapi.com.br/json/last/BTC-USD")
dolar_real=requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
euro_real=requests.get("https://economia.awesomeapi.com.br/json/last/EUR-BRL")

print(f"REQUISIÇÃO DO BITCOIN(BTC) FOI:{btc_dolar} \tCOTAÇÃO{btc_dolar.json()}")
print(f"REQUISIÇÃO DO DOLAR(USD) FOI:{dolar_real} \tCOTAÇÃO{dolar_real.json()}")
print(f"REQUISIÇÃO DO EURO(EUR) FOI:{euro_real} \tCOTAÇÃO{euro_real.json()}")

