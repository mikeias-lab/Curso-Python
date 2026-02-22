'''Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

#minha solução

n = int(input('Digite um número inteiro para converção: '))
print('-=' * 5, '{}'.format(n), '-=' * 5)
conv = int(input('Digite o opção que deseja converter:\n[ 1 ] para converter em BINÁRIO\n[ 2 ] para converter em OCTAL'
                 '\n[ 3 ] para converter em HEXADECIMAL\n'))
if conv == 1:
    print('O número {} em BINÁRIO é: {}'.format(n, bin(n)[2:]))
elif conv == 2:
    print('O número {} em OCTAL é: {}'.format(n, oct(n)[2:]))
elif conv == 3:
    print('O número {} em HEXADECIMAL é: {}'.format(n, hex(n)[2:]))
else:
    print('Você digitou um comando inválido')
