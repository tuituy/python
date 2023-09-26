pessoas = []
pessoa = []
maiorpeso = []
menorpeso = []


total = 0


resp = 'S'
while resp == 'S':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if total == 0:
        maiorpeso.append(pessoa[:])
        menorpeso.append(pessoa[:])
        #
    total +=1
    if pessoa[1] > maiorpeso[0][1] or pessoa[1] == maiorpeso[0][1]:
        maiorpeso.append(pessoa[:])
        if pessoa[1] > maiorpeso[0][1]:
            del maiorpeso[0]


    elif pessoa[1] < menorpeso[0][1] or pessoa[1] == menorpeso[0][1]:
        menorpeso.append(pessoa[:])
        if pessoa[1] < menorpeso[0][1]:
            del menorpeso[0]
    print(maiorpeso)  #
    print(menorpeso)  #




    pessoa.clear()



print('=-'*40)
print(f'Ao todo, você cadastrou {total} pessoas.')
print(f'O maior peso foi de {maiorpeso[0][1]}. Peso de {maiorpeso[0,0]}')
print(f'O menor peso foi de {menorpeso[0][1]}. Peso de {menorpeso[0,0]}')

