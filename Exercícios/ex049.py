'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

#minha solução

t = int(input('Digite um número para ver sua tabuada: '))
print('_' * 20)
for c in range(1, 11):
    print('{} * {} = {}'.format(t, c, t*c))
print('_' * 20)
