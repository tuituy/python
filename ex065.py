v1 = 0
v2 = 0
media = 0
r = ''
cont = 1
maior = 0
menor = 0
while r != 'N':
    v1 = int(input('Digite um número para saber sua média: '))
    if cont == 1:
        menor = v1
        maior = v1
        cont += 1
    else:
        cont += 1
        v2 = v1 + v2
        v1 = 0

    if v1 < menor :
        menor = v1
    elif v1 > maior:
        maior = v1


    print(media)

    r = print(input('Deseja continuar? [s/n]').upper())
else:
    media = (v1 + v2) / cont
    print ('A média entre todos os valores foi {}, o MENOR valor foi {} e o MAIOR valor foi {}'.format(media,menor,maior))


