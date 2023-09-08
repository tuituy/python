v1 = 0
v2 = 0
v3 = 0
cont = 0
while v1 != 999:
    v1 = int(input('Adicione um número a conta: '))
    cont += 1
    v3 = v2 + v1
    if v1 != 999:
        print('{} + {} = {}'.format(v2, v1, v3))
        v2 = v3
    else:
        v3 = v3 - 999
        print('Fim, a soma total dos {} números foi {}'.format(cont - 1,v3))

