from random import randint
n = 0
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valores sorteados foram: ',end='')

for n in numeros:
    print(f'{n} ',end=' ')

print(f'\nO Maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')