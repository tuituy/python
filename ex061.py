ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao termo: '))

a1 = ptermo
a2 = razao

fim = 0
while fim != 10:
    a2 = a1 + a2
    if fim == 0:
        print ('{}'.format(a1), end=' ')
    else:
        print('{}'.format(a2),end=' ')
    fim += 1
print('Fim')