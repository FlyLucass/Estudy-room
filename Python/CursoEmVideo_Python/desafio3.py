red_bold='\033[1;31m'
green_bold='\033[1;32m'
none_style='\033[0m'

print('calculando número')
N1=float(input('Digite o 1°Número '))
N2=float(input('Digite o 2°Número '))
resul=N1+N2
print(f'A soma entre:{red_bold}{N1}{none_style} é {red_bold}{N2}{none_style}= {green_bold}{resul}{none_style}')