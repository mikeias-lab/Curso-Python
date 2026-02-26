'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- A vista dinheiro/cheque: 10% desconto     - em até 2x no cartão: preço normal
- A vista no cartão: 5% desconto            - 3x ou mais no cartão: 20% de juros'''

#minha solução

print('='*10, 'LOJA SILVA', '='*10)
print('{:=^40}'.format(' LOJA SILVA ')) #outra opção para o nome da loja

preço = float(input('Qual o valor total da compra? R$'))
print('FORMAS DE PAGAMENTO'
      '\n[ 1 ] À vista dinheiro/cheque:'
      '\n[ 2 ] À vista no cartão:'
      '\n[ 3 ] 2x no cartão:'
      '\n[ 4 ] 3x ou mais no cartão:')
pagamento = int(input('Qual é a opção? '))
if pagamento == 1:
    desconto = preço - (preço * 10 / 100)
    print('Você terá 10% de desconto, então vai ficar R${:.2f}'.format(desconto))
elif pagamento == 2:
    desconto = preço - (preço * 5 / 100)
    print('Você terá 5% de desconto, então vai ficar R${:.2f}'.format(desconto))
elif pagamento == 3:
    print('Em 2x no cartão, não temos juros, então vai ficar 2x de R${:.2f}'.format(preço / 2))
elif pagamento == 4:
    juros = preço + (preço * 20 /100)
    quantidade = int(input('Em quantas parcelas? '))
    parcelas = juros / quantidade
    print('Sua compra ficou {}x de R${:.2f} COM JUROS.'
          '\nO valor total da sua compra ficou R${:.2f}'.format(quantidade, parcelas, juros))
else:
    print('VOCÊ DIGITOU UMA OPÇÃO INVÁLIDA')
