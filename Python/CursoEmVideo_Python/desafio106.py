def interactive_help_manual():
    
    print(f"\033[1;30;43m{'-'*164}")
    print("SISTEMA DE AJUDA= HELP() ")
    print(f"{'-'*164}\033[0m")
    while True:
        fuc=str(input("FUNCÃO OU BIBLIOTECA: "))
        if fuc=='FIM' or fuc=='fim':break
        print(f"\033[1;31;42m")
        print(help(fuc))
        print(f"\033[0m")
    
    print(f"\033[1;32;41m{'-'*164}")
    print("PROGRAMA ENCERRADO!!!")
    print(f"{'-'*164}\033[0m")

interactive_help_manual()
