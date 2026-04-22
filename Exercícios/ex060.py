'''from math import factorial
num = int(input('Digite um número para calcular o seu fatorial: '))
fatorial = factorial(num)
print(fatorial)'''

from math import factorial
num = int(input('Digite um número para calcular o seu fatorial: '))
c = num
print('Calculando {}! '.format(num), end='')
fat = factorial(num)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(fat))