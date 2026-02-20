#minha solução
frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.upper().find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.upper().rfind('A')+1))

#solução do professor
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
