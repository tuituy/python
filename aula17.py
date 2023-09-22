lanche = [2,3,4]#lista
lanche.append(3)# coloca um elemento no fim da lista
lanche.insert(0,0)
del lanche[3] # remove pela chave
lanche.remove(3)# remove elemento pelo nome
lanche.pop() #retira o ultimo elemento
if 3 in lanche:
    lanche.remove(3)
valores = list(range(4,11))
valores1 = [8,2,5,4,9,3,0]
valores.sort()
valores.sort(reverse=True)
len(valores)
print(lanche)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

val = list()
for cont in range (0,5):
    val.append(int(input('Digite um valor: ')))
print(val)
a = [2,3,4,7]
b = a[:]# dessa forma ele cria uma cópia, sem o [:] ele liga uma lista na outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')