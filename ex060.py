
num = int(input('Digite um número para saber o seu fatorial: '))
f = 1
print('Calculando {}!'.format(num))
while num > 0:
    print('{}'.format(num),end=' ')
    print(' x ' if num > 1 else '=',end= ' ')
    f *= num
    num-=1
print('{}'.format(f))

