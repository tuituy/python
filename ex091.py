from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
ranking = list()

for c in range (1,5):
    jogador[f'jogador{c}'] =  randint(1,6)


for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print('== RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
print('-='*30)

