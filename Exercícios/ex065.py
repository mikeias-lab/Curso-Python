cont = 'S'
tot = med = soma = maior = menor = 0
while cont in 'Ss':
    num = int(input('Digite um número: '))
    tot += 1
    soma += num
    med = soma / tot
    if tot == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont = str(input('Quer continuar [S/N]: '))
print('total {} media {:.2f}'.format(tot, med))
print('o maior número digitado foi {} e o menor número digitado foi {}'.format(maior, menor))
