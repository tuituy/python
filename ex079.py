lista = []
cont = 'S'
num = 0


while cont in 'Ss':
    num =int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...' )
    else:
        print('Valor duplicado! Não vou adicionar...')

    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if cont in 'Nn':
        break

print(f'Você digitou os valores {sorted(lista)} ')
