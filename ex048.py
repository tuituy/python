s = 0
cont = 0
for c in range (1,500,2):

    if c % 3 == 0:
        s += c
        cont += 1
print('A soma dos valores divisíveis por 3 é de {} e a quantidade de valores somados é {}.'.format(s,cont))
