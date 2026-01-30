salário = float(input('Qual é o seu salário? R$'))
novo = salário + (salário*15/100)
print('Só R${:.2f}? Eu vou te dar 15% de aumento, então você vai receber R${:.2f} a partir de agora!'.format (salário, novo))
