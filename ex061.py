ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao termo: '))


fim = 0
while fim != 10:
    print ('{}'.format(ptermo), end=' ')
    ptermo += razao
    fim += 1
print('Fim')
