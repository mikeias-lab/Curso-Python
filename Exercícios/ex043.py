'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso        - 25 até 30: Sobrepeso
- Entre 18.5 e 25: Peso ideal           - 30 até 40: Obesidade
                                        - Acima de 40: Obesidade mórbida'''

#minha solução

print('-='*10)
print('CÁLCULO DE IMC')
print('-='*10)
altura = float(input('Digite sua altura (ex.: 1.70): '))
peso = float(input('Digite seu peso em KG: '))
imc = peso / (altura * altura)
print('O seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
