from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

cont = 0
while True:

    total = 0
    tipo = '2'

    jogador = int(input('Diga um valor: '))

    computador = int(randint(1,10))
    total = jogador + computador

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]

    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', 'DEU PAR' if total % 2== 0 else 'DEU IMPAR')
    if tipo == 'P':
       if total % 2 == 0:
           print('Você VENCEU!!')
           cont += 1
       else:
           print('Você PERDEU!')
           break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!!')
            break


print(f'GAME OVER! Você venceu {cont} vezes. ')

