from math import sqrt
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
num = sqrt(a**2+b**2)
print('A hipotenusa vai medir {:.2f}' .format(num))
