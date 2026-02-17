n1 = float(input('Quanto você vendeu ontem? '))
n2 = float(input('Quanto você vendeu hoje? '))
s = n1 + n2
print('A sua meta nesses dois dias eram R$1000,00 e você vendeu R${}'.format(s))
if s >= 1000.00:
    print('Parabéns, vendeu muito!')
else:
    print('Está demitido por não entregar a meta proposta')
