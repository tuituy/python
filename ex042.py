r1 = float(input('Digite a primeira reta '))
r2 = float(input('Digite a segunda reta '))
r3 = float(input('Digite a terceira reta '))



if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('temos um triângulo ', end='')
    if r1 == r2 == r3:
        print('equilátero.')
    elif r1 != r2 != r3 != r1 :
        print('escaleno.')
    else:
        print('isóceles')
else:
    print('Isso ai n dá um triângulo não!')
