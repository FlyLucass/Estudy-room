numeros=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

print("VAMOS GERAR O NÚMERO POR EXTENSO ")
escolhar_user=int(input("Digite um numero entre 0 e 20: "))
if escolhar_user>20:
    while escolhar_user>20:
        escolhar_user=int(input("Enquanto o programa não for entre 0 e 20, não podemos continuar: "))




print(f"O número {escolhar_user} por escrito é: {numeros[escolhar_user]}")