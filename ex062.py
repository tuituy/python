ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao termo: '))


fim = 10
while fim > 0:
    print ('{}'.format(ptermo), end=' ')
    ptermo += razao
    fim -= 1
    if fim == 0:
        fim = int(input('\nSe deseja continuar digite quantos mais, ou digite 0 para sair: '))
        if fim == 0:
            print('Fim')
            fim = -1

