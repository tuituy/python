from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
cont = 0
total = 0

while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]')).upper()
    computador = int(randint(1,10))
    total = jogador + computador


    if escolha == 'P' and total % total == 0:
        print('_' * 20)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, DEU PAR')
        print('_' * 20)
        print('Você VENCEU!')
        print('Vamos jogar novamente ...')
        cont += 1
    else:
        print('_' * 20)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, DEU IMPAR')
        print('_' * 20)
        print('Você PERDEU!')
        print('_' * 20)
        break
print(f'GAME OVER! Você venceu {cont} vezes. ')

