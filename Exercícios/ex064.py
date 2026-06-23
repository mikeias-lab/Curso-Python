total = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        total += 1
        soma += num
print('Você digitou {} números e a soma entre eles foi {}.'.format(total, soma))
