'''Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.'''

#minha solução

casa = float(input('Qual o valor do imóvel? R$'))
salário = float(input('Qual a sua renda mensal? R$'))
anos = int(input('Em quantos anos você vai quitar o imóvel? '))
meses = anos * 12
prestação = casa / meses
if prestação >= salário * 30 / 100:
    print('Sinto muito, as parcelas ficariam R${:.2f}, esse valor exede 30% do seu salário. \033[31mEMPRÉSTIMO REPROVADO\033[m'.format(prestação))
else:
    print('Você vai pagar R${:.2f} de prestação. \033[32mPARABÉNS! SEU EMPRÉSTIMO FOI APROVADO'.format(prestação))
