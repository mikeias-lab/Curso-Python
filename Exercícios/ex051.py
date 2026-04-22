'''programa que leia o primeiro termo e a razão de uma PA. no final, mostre os
10 primeiros termos dessa progressão.'''

#não consegui fazer

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + 1, razão):
    print('{} => '.format(c), end='')
print('FIM')
