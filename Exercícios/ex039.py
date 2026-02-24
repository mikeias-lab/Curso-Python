'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

#minha solução

from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade < 18 and idade > -1:
    falta = 18 - idade
    alistamento = falta + date.today().year
    print('Você tem {} anos\nAinda faltam {} anos para se alistar\nSeu ano de alistamento será em {}.'
          .format(idade, falta, alistamento))
elif idade > 18 and idade < 45:
    passou = idade - 18
    alistamento = date.today().year - passou
    print('Você tem {} anos.\nVocê deveria ter se alistado há {} anos\nSeu alistamento foi em {}.'
          .format(idade, passou, alistamento))
elif idade == 18:
    print('Você tem {} anos\nDeve se alistar nesse ainda esse ano, em {}'.format(idade, date.today().year))
elif idade >= 45: #o período como reservista no Exército encerram-se ao final do ano em que o cidadão completa 45 anos de idade
    print('Você concluiu o serviço militar obrigatório, OBRIGADO PELOS SEUS SERVIÇOS!!!')
elif idade < 0:
    print('Você ainda nem nasceu kkk')
