import statistics;
alunos=[]
aluno=[]
notas=[]

continuar=str('')

while not continuar=='n':
    aluno.append(str(input("Digite o nome do Aluno: ")))
    notas.append(float(input("Nota 1: ")))
    notas.append(float(input("Nota 2: ")))
    aluno.append(notas[:])
    alunos.append(aluno[:])
    continuar=str(input("Que continuar(S/N): ")).casefold()
    if continuar!='s' or continuar!='n':
        while continuar!='s' and continuar!='n':
            continuar=str(input("Apenas(S/N): ")).casefold()
    notas.clear()
    aluno.clear()

contador=int(0)
for i in alunos:
    print(f"\n{contador}° {i[0]} sua média foi:{statistics.mean(i[1])} ")
    contador+=1

while True:
    interroper=int(input("\nQual nota você deseja de acordo com a posição de cada aluno: "))
    if interroper==999:break
    else:print(alunos[interroper][1])



