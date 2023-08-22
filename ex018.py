
from math import sin,cos,tan,radians
angulo = float(input('Qual é o ângulo?'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(angulo,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo,cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo,tang))
