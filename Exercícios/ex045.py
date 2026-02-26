'''Crie um programa que faça o computador jogar JOKENPÔ com você'''

#minha solução

from random import choice
from time import sleep
list = ('PEDRA', 'PAPEL', 'TESOURA')
computador = choice(list)
jogador = int(input('Suas opções:'
                    '\n[ 0 ] PEDRA'
                    '\n[ 1 ] PAPEL'
                    '\n[ 2 ] TESOURA'
                    '\nQual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*10)
print('Computador jogou {}\nJogador jogou {}'.format(computador, list[jogador]))
print('-='*10)
if jogador == 0:
    if computador == 'PEDRA':
        print('EMPATOU')
    elif computador == 'PAPEL':
        print('COMPUTADOR VENCE')
    elif computador == 'TESOURA':
        print('JOGADOR VENCE')
elif jogador == 1:
    if computador == 'PEDRA':
        print('JOGADOR VENCE')
    elif computador == 'PAPEL':
        print('EMPATOU')
    elif computador == 'TESOURA':
        print('COMPUTADOR VENCE')
elif jogador == 2:
    if computador == 'PEDRA':
        print('COMPUTADOR VENCE')
    elif computador == 'PAPEL':
        print('JOGADOR VENCE')
    elif computador == 'TESOURA':
        print('EMPATOU')
else:
    print('VOCÊ DIGITOU UM COMANDO INVÁLIDO')
