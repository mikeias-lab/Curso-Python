print('_'*20)
print('Sequência Fibonacci')
print('_'*20)
termos = int(input('Quantos termos você quer mostrar? '))
primeiro = 0
segundo = 1
print('{} => {} => '.format(primeiro, segundo), end='')
cont = 3
while cont <= termos:
    t3 = primeiro + segundo
    print('{} => '.format(t3), end='')
    primeiro = segundo
    segundo = t3
    cont += 1
print('FIM')