'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados são iguais
- ISÓSCELES: dois lados são iguais
- ESCALENO: todos os lados são diferentes'''

#minha solução

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s1 == s2 == s3:
    print('Os segmentos acima PODEM FORMAR triângulo e são EQUILÁTERO!')
elif s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s1 == s2 or s1 == s3 or s2 == s3:
    print('Os segmentos acima PODEM FORMAR triângulo e são ISÓSCELES!')
elif s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os segmentos acima PODEM FORMAR triângulo e são ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

#solução do professor

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles!')
    else:
        print('Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
