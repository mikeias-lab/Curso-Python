real = float(input('Quanto dinheiro você tem na carteira? R$'))
dólar = real / 5.19
euro = real / 6.21
iene = real / 0.034
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dólar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥{:.2f}'.format(real, iene))
