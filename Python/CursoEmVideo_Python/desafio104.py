
def leiaint(nub):
    if nub.isnumeric():
        print(f"Número digitado foi {nub}")
    else:
        while not nub.isnumeric():
            nub = input("Digite um n: ")
        print(f"Número digitado foi {nub}")

n=input("Digite um n: ")
leiaint(n)