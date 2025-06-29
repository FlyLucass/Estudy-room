
def notas(nota,sit='false'):
    
    '''
    Recebe as notas do usuario: Pode ser float!  
    Para continuar o algoritmo apenas: s=Sim / n=Não
    Para adicionar um feedback da média da turma: True=Sim / False=Não
    Retorna: Um dict com: Quatidade de notas;Maior Nota; Menor Nota; Média das notas e situação(opcional)
    '''
    
    
    informe={}
    quant_notas=int(0)
    maior=float(0)
    menor=float(0)
    media=float(0)
    for i,v in enumerate(nota):
        quant_notas+=1
        media+=v
        if i==0:
            maior=v
            menor=v
        else:
            if v>maior: maior=v
            if v<menor: menor=v
    media=media/quant_notas
    informe.update({"Quantidade de Notas":quant_notas})
    informe.update({"A maior nota":maior})
    informe.update({"A menor nota":menor})
    informe.update({"A Média da Turma":media})
    if sit!='False':
        if media>=7: informe.update({"Situação": 'Excelente!!!'})
        elif media>=6 and media<7: informe.update({"Situação": 'Razoavel'})
        else:  informe.update({"Situação": 'Ruim'})
    print(informe)
    
recebi_nota=[]
contador=int(0)
help(notas)
while True:
    contador+=1
    recebi_nota.append(float(input(f"Digite uma {contador}° nota: ")))
    contin_alg=str(input("Deseja continuar? ")).casefold()
    if contin_alg!='n' or contin_alg!='s':
        while contin_alg!='n' and contin_alg!='s':
                contin_alg=str(input("Apenas (s/n)")).casefold()
    if contin_alg=='n':break
situa=str(input("Você deseja adiciona uma situação da turma? ")).capitalize()
if situa!='True' or situa!='False':
    while situa!='True' and situa!='False':
        situa=str(input("Você deseja adiciona uma situação da turma? ")).capitalize()
notas(recebi_nota,situa)
    