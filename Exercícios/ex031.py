'''Desenvolva um programa que pergunte a distância de uma viagem
em km. Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 para viagens mais longas.'''

#minha solução

d = float(input('Qual a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
if d <= 200:
    print('E o preço da passagem será R${:.2f}'.format(d * 0.5))
else:
    print('E o preço da passagem será R${:.2f}'.format(d * 0.45))

#solução do professor

distância = float(input('Qual a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.5 if distância <= 200 else distância * 0.45
print('E o preço da passagem será R${:.2f}'.format(preço))
