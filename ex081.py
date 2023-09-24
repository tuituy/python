lista = []
num = 0
cont = 'S'

while cont in 'Ss':
    num = int(input('Digite um valor: '))
    lista.append(num)
    cont = str(input('Quer continuar? [S/N]'))

print('=-'*30)
print(f'Você digitou {len(lista)} elementos.')

print(f'Os valores em ordem descrescente são {sorted(lista, reverse = True)}')

pos = 0


while pos != len(lista):
    if 5 == lista[pos]:
        print('O valor 5 faz parte da lista!')
        break
    pos +=1
if pos == len(lista):
    print('O valor 5 não foi encontrado na lista!')




