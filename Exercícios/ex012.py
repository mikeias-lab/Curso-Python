preço = float(input('Qual é o preço do produto? R$'))
desc = preço - (preço * 5 / 100)
aumento =  preço + (preço * 7 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f} \nMas na notinha fica R${:.2f} com 7% de aumento'.format(preço, desc, aumento))


# são 5% de desconto a vista
# são 7% a mais na notinha