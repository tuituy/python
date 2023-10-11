def contagem(inicio,fim,passo,*num):
    print('-=' * 30)
    print(*num)
    for contagem in range(inicio,fim,passo):

        print(contagem,end=' ')
    print('Fim')


contagem(1,11,1,'Contagem de 1 até 10 de 1 em 1')
contagem(10,-1,-2,'Contagem de 10 até 0 de 2 em 2')
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))

passo = int(input('Passo: '))
if fim <= 0:
    fim -= passo
elif fim < 0:
    fim += passo
contagem(inicio,fim,passo,f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')#transforma em positivo
