dist_in_km=int(input("Vamos calcular o vlaor da sua viagem! \nDigite quantos KM e até o destino "))
if dist_in_km <= 200: valor=float(0.50*dist_in_km); print("o valor da viagem e: R${}".format(valor))
elif dist_in_km>200: valor=float(0.45*dist_in_km); print("o valor da viagem e: R${}".format(valor))