'''Escrever um programa que faça o computador pensar em um número entre 0 e 5
pedir para o usuário tentar advinhar o número que computador pensou
e por fim, o pragrama vai dizer se o usuário acertou ou não'''

#minha solução

from random import randint
n = randint(0 ,5)
print('Vou pensar num número entre 0 e 5, tente advinhar!')
r = int(input('Qual número eu pensei? '))
if r == n:
    print('Parabéns, o número escolhido realmente foi {}'.format(n))
else:
    print('Que pena, não foi o {}, e sim {}, mais sorte na próxima!'.format(r, n))
'''
#solução do professor

from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
    '''
