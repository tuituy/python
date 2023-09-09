primeirovalor = 0
segundovalor = 0
media = 0
r = ''
cont = 1
maior = 0
menor = 0
while r != 'N':
    primeirovalor = int(input('Digite um número para saber sua média: '))
    segundovalor = int(input('Digite o número para saber sua média: '))
    if cont == 1:
        media = primeirovalor + segundovalor / 2
        menor = primeirovalor
        maior = primeirovalor
        v2 = v1 + v2
        v1 = 0
        cont += 1
        if cont < 1:
            media = v1 + v2 / cont
    if v1 < menor :
        menor = v1
    elif v1 > maior:
        maior = v1


    print(media)

    r = print(input('Deseja continuar? [s/n]').upper())
    if r == 'N':
        media = (v1 + v2) / cont
        print('A média entre todos os valores foi {}, o MENOR valor foi {} e o MAIOR valor foi {}'.format(media, menor,maior))

