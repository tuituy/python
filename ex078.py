

maior = 0
menor = 0
valor = []
for c in range (0,5):
    valor.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = valor[c]
        menor = valor[c]
    elif valor[c] > maior:
        maior = valor[c]
    elif valor[c] < menor:
        menor = valor[c]
print('=-'*30)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} nas posições ',end='')
for i, v in enumerate (valor):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ',end='')
for i,v in enumerate (valor):
    if v == menor:
        print(f'{i}...',end='')
print()
