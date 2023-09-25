lista = []
pares = []
impares = []
continua = 'S'

while continua == 'S':
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    lista.append(num)
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
else:
    print(f'A lista completa é {lista}')
    print(f'A lista de pares é {pares}')
    print(f'A lista de ímpares é {impares}')


