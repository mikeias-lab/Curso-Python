import math
an = float(input('Digite o angulo que você deseja: '))
rad = math.radians(an)
se = math.sin(rad)
co = math.cos(rad)
ta = math.tan(rad)
print('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem o TANGENTE de {:.2f}'.format(an, se, an, co, an, ta))
