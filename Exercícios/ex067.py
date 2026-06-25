while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    if num > 0:
        print('_'*20)
        for t in range (1, 11):
            resultado = num * t
            print(f'{num} x {t} = {resultado}')
        print('_' * 20)
    else:
        break
print('_' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
