from random import randint
from time import sleep
computador = randint(0,10) # pc escolhe um número
cont = 1
tentativas = 1
print('*-'*21)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('*-'*21)

while cont != 0:
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        cont = 0
        print('\033[30;42mPARABÉNS! Você consegiu me vencer!, Realmente pensei no {}\033[m'.format(computador))
        print('Você precisou de {} tentativas.'.format(tentativas))

    else:
        if jogador < computador:
            print('é mais...')
        elif jogador > computador:
            print('é menos...')
        print('\033[0;30;41mErrou,Tente novamente!\033[m')
        tentativas = tentativas + 1
        




