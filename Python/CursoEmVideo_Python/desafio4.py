bold='\033[1m'
none='\033[0m'
cinza_change='\033[7;30;47m'
under='\033[4m'
print('Check do que e digitado')
cite=input('Digite algo')
print('{}{}{} {}{}{}'.format(bold,'Qual o tipo?',none,cinza_change,type(cite),none))
print('{}{}{} {}{}{}'.format(bold,'isso é feito em letra:',none,under,cite.isalpha(),none))
print('{}{}{} {}{}{}'.format(bold,'é em número:',none,under,cite.isnumeric(),none))

print(int(6/2))