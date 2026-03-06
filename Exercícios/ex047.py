'''Crie um programa que mostre na tela todos os números pares
que estão no intervalo entre 1, 50.'''

#minha solução

print('Os número PARES que estão entre 1 e 50 são:')
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
