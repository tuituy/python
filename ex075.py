
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
numeros = (num1,num2,num3,num4)

numero9 = 0
pares = 0
if num1  % 2 == 0:
    pares += 1
elif num2 % 2 == 0:
    pares += 1
elif num3 % 2 == 0:
    pares += 1
elif num4 % 2 == 0:
    pares += 1




print(f'Você digitou os valores {numeros}')
if num1 or num2 or num3 or num4 == 9:
    numero9+=1
    print(f'O valor 9 apareceu {numero9} vezes.')

for pos,numeros in enumerate(numeros):
    if numeros == 3:
        print(f'O valor 3 apareceu na {pos+1}ª posição.')

if num1  % 2 == 0:
    pares += 1
elif num2 % 2 == 0:
    pares += 1
elif num3 % 2 == 0:
    pares += 1
elif num4 % 2 == 0:
    pares += 1



print(f'Os valores pares digitados foram {pares}')



