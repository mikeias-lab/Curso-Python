'''programa que leia um número inteiro e diga se ele é ou não um número primo.'''

#solução do professor

num = int(input('Digite um número: '))
total = 0 #variante pra somar quantas vezes foram divididos
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mOnúmero {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('Então ele É UM NÚMERO PRIMO')
else:
    print('Então ele NÃO É UM NÚMERO PRIMO')
