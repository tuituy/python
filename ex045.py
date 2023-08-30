from random import randint

pedra = 0
papel = 1
tesoura = 2

computador = randint(pedra,tesoura)


print('{:=^40}'.format(' JO KEN PO!!! '))


print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual a sua jogada? '))

if jogada == computador :
    print('Empate!, escolhi o mesmo que você.')

elif jogada == 0 and computador == 1:
    print('Perdeu!, escolhi papel.')
elif jogada == 0 and computador == 2:
    print('Ganhou!, escolhi teroura')

elif jogada == 1 and computador == 0:
    print('Ganhou!, escolhi pedra.')
elif jogada == 1 and computador == 2:
    print('Perdeu!, escolhi tesoura')

elif jogada == 2 and computador == 0:
    print('Perdeu!, escolhi pedra.')
elif jogada == 2 and computador == 1:
    print('Ganhou, escolhi pedra.')
else:
    print('Opção inválida!!!')



print(computador)


