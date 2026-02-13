#minha solução
nome = str(input('Digite seu nome completo: ')).strip().title().split()
print('Muito prazer em te conhecer!')
print('Seu primero nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))

#solução do professor
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
