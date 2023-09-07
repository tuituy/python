ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao termo: '))


fim = 0
while fim != 10:
    print ('{}'.format(ptermo), end=' ')
    ptermo += razao
    fim += 1
    if fim == 1:
        proxtermo = int(input('Se deseja continuar digite quantos mais, ou digite 0 para sair: '))
        fim = 0
        ptermo += razao
        fim += 1



print('Fim')
