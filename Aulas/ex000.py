n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('a soma dos valores é {}'.format(s))
print(f'a soma dos valores é {s}') #ultilizando a fstring
