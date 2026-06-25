print('=-' * 20, '\nVAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
cont = 0
while True:
    num = int(input('Diga um valor: '))
    pi = str(input('PAR OU ÍMPAR (P/I): ')).upper()
    print('=-' * 20)
    from random import randint
    comp = randint(1, 10)
    soma = num + comp
    cont += 1
    if soma % 2 != 0:
        i = 'I'
        print(f'Você jogou {num} e o computador jogou {comp}. Total de {soma} deu ÍMPAR')
        if pi == i:
            print('-' * 20, '\nVocê VENCEU!\nVamos jogar novamente...')
            print('-'*20)
        else:
            print(f'Game Over! Você venceu {cont - 1} vezes.')
            break
    else:
        p = 'P'
        print(f'Você jogou {num} e o computador jogou {comp}. Total de {soma} deu PAR')
        if pi == p:
            print('-' * 20, '\nVocê VENCEU!\nVamos jogar novamente...')
            print('-' * 20)
        else:
            print(f'Game Over! Você venceu {cont - 1} vezes.')
            break
