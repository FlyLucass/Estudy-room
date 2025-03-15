def area(base,altura):
    calc=float(base*altura)
    print(f"A área {base}x{altura} é : {calc}cm²")
    
def linha_div():
    print('-'*30)

 
base=float(input(f"VAMOS CALCULAR A ÁREA!!! \n\nDigite o comprimento "))
linha_div()
altura=float(input("Digite a Largura: "))
linha_div()
area(base,altura)

