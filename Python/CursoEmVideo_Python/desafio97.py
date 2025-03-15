def escreva(user):
    def i_segue():print('~',end='')
    i_segue()
    print('~'*len(user),end='')
    print('~')
    print(f" {user}")
    i_segue()
    print('~'*len(user),end='')
    print('~')
    

    
    
    
user=str(input("Digite algo: ")).capitalize().strip()
escreva(user)



