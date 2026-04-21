from time import sleep
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    escolha = int(input('>>>>> Qual a sua opção? '))
    if escolha == 1:
        soma = v1 + v2
        print('A soma de {} com {} é {}'.format(v1, v2, soma))
        print('=-' * 20)
        sleep(2)
    elif escolha == 2:
        multi = v1 * v2
        print('A multiplicação de {} com {} é {}'.format(v1, v2, multi))
        print('=-' * 20)
        sleep(2)
    elif escolha == 3:
        if v1 > v2:
            print('O maior valor digitado foi {}'.format(v1))
        elif v1 == v2:
            print('Ambos os valores digitados são iguais')
        else:
            print('O maior valor digitado foi {}'.format(v2))
        print('=-' * 20)
        sleep(2)
    elif escolha == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
    elif escolha > 5 or escolha <= 0:
        print('\033[31mDigite um comando válido:\033[m')
print('Fim do programa! Volte sempre!')
