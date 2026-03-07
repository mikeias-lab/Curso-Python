'''programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

#minha solução

soma = 0
for n in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print(soma)
