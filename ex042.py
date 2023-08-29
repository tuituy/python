r1 = float(input('Digite a primeira reta '))
r2 = float(input('Digite a segunda reta '))
r3 = float(input('Digite a terceira reta '))



if r1 == r2 and r1 == r3:
    print('Temos um triângulo Equilátero.')
elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1 :
    print('Temos um triângulo Isóceles.')
elif r1 != r2 and r2 != r3:
    print('Temos um triângulo Escaleno.')
else:
    print('Isso ai n dá um triângulo não!')
