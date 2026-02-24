'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com sua idade:
- Até 9 anos: MIRIN                 - Até 19 anos: JUNIOR
- Até 14 anos: INFANTIL             - Até 25 anos: SÊNIOR
                                    - Acima: MASTER'''

#minha solução

from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if 0 <= idade <= 9:
    print('Você tem {} anos e está na categoria MIRIN.'.format(idade))
elif 9 < idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('Você tem {} anos e está na categoria JUNIOR.'.format(idade))
elif 19 < idade <= 25:
    print('Você tem {} anos e está na categoria SÊNIOR.'.format(idade))
elif 25 < idade:
    print('Você tem {} anos e está na categoria MASTER.'.format(idade))
else:
    print('Você nem nasceu ainda kkk')
