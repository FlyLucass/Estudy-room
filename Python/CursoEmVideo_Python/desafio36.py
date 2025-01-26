age=int(input("vamos saber se voce não está no tempo do alistamento, deve ou ja passou do tempo \ndigite seu ano de nasimento: "))
age=2024-age
temp_p=age-18
temp_b=17-age

if age<17:print(f"Não está no tempo de se alistar, ainda faltam {temp_b} anos.")
elif age>18:print(f"Já passou do tempo do alistamento, procure mais informaçoes com urgencia,você está á {temp_p} ano atrasado")
else: print("você ja está no tempo de seu alistamento")