média = 0
velho = 0
nomevelho = ''
mulher = 0
for p in range(1, 5):
    print('--- {}ª PESSOA ---'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    média += (idade) / 4
    if p == 1:
        maior = idade
        nomevelho = nome
    else:
        if idade > maior:
            maior = idade
            nomevelho = nome
    if sexo == 'F':
        mulher += 1
print('A média de idade do grupo é de {} anos'.format(média))
print('A pessoa mais velha do grupo tem {} anos e se chama {}.'.format(maior, nomevelho))
print('Ao todo são {} mulheres'.format(mulher))
