frase = str(input('Digite uma frase: ')).strip().upper() #strip vai tirar os espaços e upper vai jogar pra maiúsculo
palavras = frase.split() #identifica e separa cada palavra
junto = ''.join(palavras) #junta as palavras eliminando os espaços
inverso = ''
for letra in range(len(junto) -1, -1 , -1):
    inverso += junto[letra]
if inverso == junto:
    print('O inverso de {} é {}\nA frase digitada É UM PALÍNDROMO!'.format(junto, inverso))
else:
    print('O inverso de {} é {}\nA frase digitada NÃO É UM PALÍNDROMO!'.format(junto, inverso))
