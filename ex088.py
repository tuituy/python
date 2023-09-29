from random import randint
from time import sleep
jogo = []
print('-'*30)
print('      JOGA NA MEGA SENA     ')
print('-'*30)


r = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3,end='')
print(f' SORTEANDO {r} JOGOS  ',end='')
print('-='*3)

for i in range(0,r):
    for c in range(0,6) :
        num = randint(1,60)
        while num not in jogo:
            jogo.append(num)

        jogo.sort()

    sleep(1)
    print(f'Jogo {i+1}: {jogo}')
    jogo.clear()
print('-='*5,end='')
print(' < BOA SORTE! > ',end='')
print('-='*5)

