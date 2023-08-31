from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep (1)
print('PO!!!')
print('-='*11)
print('O computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0:#pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('Jogada inválida!')
elif computador == 1:#papel
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print ('Empate!')
    elif jogador == 2:
        print ('Jogador Vence')
    else:
        print('Jogada inválida!')

elif computador == 2:#tesoura
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Computador Vence!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida!')
