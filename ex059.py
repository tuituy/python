sairdoprograma = 0
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

while sairdoprograma == 0:
    r = int(input('''O que deseja fazer?:
    [ 1 ] somar
    [ 2 ]multiplicar
    [ 3 ]maior
    [ 4 ]novos números
    [ 5 ]sair do programa'''))
    somar = v1 + v2
    multiplicar = v1 * v2

    if r == 1:
        print('A soma entre os números é {:.2f}.'.format(somar))


    elif r == 2:
        print('A multiplicação entre os números é {}'.format(multiplicar))

    elif r == 3:
        if v1 > v2:
            print('O número {} é maior.'.format(v1))
        elif v2 > v1:
            print('O número {} é maior.'.format(v2))
        elif v1 == v2:
            print('Os dois números são iguais.')

    elif r == 4:
        v1 = float(input('Digite o primeiro valor novamente: '))
        v2 = float(input('Digite o segundo valor novamente: '))

    elif r == 5:
        sairdoprograma = 1

        print('Fim.')

