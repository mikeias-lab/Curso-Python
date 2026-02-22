'''Escreva um programa que leia dois número inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

#minha solução

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('\033[32mO primeiro valor É MAIOR!\033[m')
elif n2 > n1:
    print('\033[36mO segundo valor É MAIOR!\033[m')
elif n1 == n2:
    print('\033[34mNão existe valor maior, OS DOIS SÃO IGUAIS!\033[m')
