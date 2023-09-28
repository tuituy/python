matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
somat = 0
maiors= 0
for l in range(0,3):
    for c in range(0,3):
        num = matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]'))
        if num % 2 == 0:
            soma += num

for s in range(0,3):
    somat += matriz[s][2]
print('-='*30)

maiors = matriz[1][0]
if matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    maiors = matriz[1][1]

elif matriz[1][2] > matriz[1][0] and matriz[1][2] > matriz[1][1]:
    maiors = matriz[1][2]
    

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
print('-='*30)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {somat}.')
print(f'O maior valor da segunda linha é {maiors}.')



