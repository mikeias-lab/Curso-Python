from datetime import date
anoatual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = anoatual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tivemos {} pessoas menores de idade'.format(totmenor))
