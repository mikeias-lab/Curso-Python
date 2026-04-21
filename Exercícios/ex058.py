from random import randint
sort = randint (0, 10)
print('\033[36mSOU SEU COMPUTADOR...\033[m')
print('Acabei de pensar em um número entre 0 e 10.\nTente advinhar qual número eu pensei:')
r = int(input('Qual o seu palpite? '))
tent = 1
while r != sort:
    if r > sort:
        r = int(input('MENOS... Tente novamente: '))
    elif r < sort:
        r = int(input('MAIS... Tente novamente: '))
    tent += 1
if tent == 1:
    print('Acertou de primeira! \033[32mParabéns\033[m')
else:
    print('Acertou com {} tentativas. \033[32mParabéns\033[m'.format(tent))
