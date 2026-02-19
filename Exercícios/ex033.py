'''Faça um programa que leia três números e
mostre qual é o MAIOR e qual é o MENOR.'''

#minha solução

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 < n2 < n3:
    print('O menor número digitado foi {} \nO maior número digitado foi {}'.format(n1, n3))
if n2 < n3 < n1:
    print('O menor número digitado foi {} \nO maior número digitado foi {}'.format(n2, n1))
if n3 < n1 < n2:
    print('O menor número digitado foi {} \nO maior número digitado foi {}'.format(n3, n2))
if n2 < n1 < n3:
    print('O menor número digitado foi {} \nO maior número digitado foi {}'.format(n2, n3))
if n1 < n3 < n2:
    print('O menor número digitado foi {} \nO maior número digitado foi {}'.format(n1, n2))
if n3 < n2 < n1:
    print('O menor número digitado foi {} \nO maior número digitado foi {}'.format(n3, n1))

#solução do professor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
