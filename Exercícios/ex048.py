'''Um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.'''

#minha solução

soma = 0
for c in range(1, 50):
    if c % 2 != 0 and c % 3 == 0:
        soma += c #precisei buscar na internet essa parte da soma
print(soma)
