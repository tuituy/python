print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))

r50 = 0
r20 = 0
r10 = 0
r1 = 0


while valor >= 50:
    r50 += 1
    valor -= 50

while valor >= 20 and valor < 50:
    r20 += 1
    valor -= 20

while valor >= 10 and valor < 20:
    r10 += 1
    valor -= 10

while valor >= 1 and valor < 10:
    r1 += 1
    valor -= 1

print(valor)


print(f'''Total de {r50} cédulas de R$50
Total de {r20} cédulas de R$20
Total de {r10} cédulas de R$10
Total de {r1} cédulas de R$1
''')
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

