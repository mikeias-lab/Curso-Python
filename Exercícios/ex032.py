'''Faça um programa que leia um ano qualquer
e mostra se ele é BISSEXTO'''

#minha solução

ano = int(input('Digite o ano para saber se é BISSEXTO ou não: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('É BISSEXTO')
else:
    print('Não é')

#solução do professor com opção de colocar o ano atual da máquina

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0:
    print('O ano {} É BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))