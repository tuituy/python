from random import randint
numeros = ' '
maior = ''
menor = ''
while len(numeros) <= 5:
    sorteio = randint(1,10)
    if numeros == ' ':
        maior = sorteio
        menor = sorteio
    elif sorteio > maior:
        maior = sorteio
    elif sorteio < menor:
        menor = sorteio
    numeros += str(sorteio)




print('Os valores sorteados foram: ', end=' ')
print (numeros)
print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')


