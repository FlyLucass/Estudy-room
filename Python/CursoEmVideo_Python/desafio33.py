print("Vamos calcular sua media")
nota1=float(input("Primeira nota: "))
nota2=float(input("Segunda nota: "))
media=(nota1+nota2)/2
if media<5: print("Reprovado")
elif media <=6.9: print("Recuperacao")
else:print("Aprovado")