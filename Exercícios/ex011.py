largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a largura da parede? '))
área = largura * altura
tinta = área / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format (largura, altura, área))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
