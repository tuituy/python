ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao termo: '))
fim = 10
cont = 0

for c in range ((ptermo),100000000000, (razao)):
    if cont < 10:
        print('{} '.format(c), end=' ')
        cont = cont +1

